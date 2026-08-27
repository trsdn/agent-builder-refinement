#!/usr/bin/env python3
"""Validate the documentation and template files in this repository.

This repository ships Markdown templates and prompts, not source code, so the
only things worth checking automatically are that the templates are well formed
and that the documentation does not point at files which do not exist.

Two checks run, both fully offline and deterministic:

1. **Front matter** - every VS Code custom agent (``.github/agents/*.agent.md``)
   and prompt (``.github/prompts/*.prompt.md``) file starts with YAML front
   matter that parses, carries the keys VS Code needs, and - for prompts -
   references an agent that actually exists in this repository.
2. **Relative links** - every relative Markdown link and image target resolves
   to a file or directory that is committed to the repository. External
   ``http(s)`` links are deliberately not fetched, so the check never depends on
   the network or on third-party uptime.

Usage::

    python scripts/validate_docs.py

Exits 0 when everything passes, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent

AGENT_DIR = REPO_ROOT / ".github" / "agents"
PROMPT_DIR = REPO_ROOT / ".github" / "prompts"

AGENT_REQUIRED_KEYS = ("description", "name")
PROMPT_REQUIRED_KEYS = ("description", "name", "agent")

FENCE_RE = re.compile(r"^\s*(?:```|~~~)")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(\s*([^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\s*\)")
SKIPPED_SCHEMES = ("http://", "https://", "mailto:", "tel:", "//")

# Verbatim copies of a Microsoft Learn article, kept in the repository so they
# can be uploaded as agent knowledge files. Their relative links resolve against
# learn.microsoft.com, not against this repository, so they are excluded from the
# link check instead of being rewritten away from the upstream wording.
VENDORED_DOCS = frozenset(
    {
        "Agent Builder Template/Write effective instructions for declarative agents.md",
        "Copilot Prompt/Write effective instructions for declarative agents.md",
    }
)


def markdown_files() -> list[Path]:
    """Return every Markdown file in the repository, sorted for stable output."""
    return sorted(
        path
        for path in REPO_ROOT.rglob("*.md")
        if ".git" not in path.parts and "node_modules" not in path.parts
    )


def split_front_matter(text: str) -> dict | None:
    """Return the raw YAML front matter block, or None when there is none."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return {"raw": "\n".join(lines[1:index])}
    return None


def check_front_matter(path: Path, required_keys: tuple[str, ...]) -> tuple[list[str], dict]:
    """Validate one agent or prompt template. Returns (errors, parsed front matter)."""
    errors: list[str] = []
    rel = path.relative_to(REPO_ROOT)
    block = split_front_matter(path.read_text(encoding="utf-8"))

    if block is None:
        errors.append(f"{rel}: missing YAML front matter delimited by '---'")
        return errors, {}

    try:
        data = yaml.safe_load(block["raw"])
    except yaml.YAMLError as exc:
        errors.append(f"{rel}: front matter is not valid YAML ({exc.__class__.__name__}: {exc})")
        return errors, {}

    if not isinstance(data, dict):
        errors.append(f"{rel}: front matter must be a YAML mapping, got {type(data).__name__}")
        return errors, {}

    for key in required_keys:
        value = data.get(key)
        if value is None:
            errors.append(f"{rel}: front matter is missing required key '{key}'")
        elif not isinstance(value, str) or not value.strip():
            errors.append(f"{rel}: front matter key '{key}' must be a non-empty string")

    tools = data.get("tools")
    if tools is not None:
        if not isinstance(tools, list) or not all(isinstance(tool, str) for tool in tools):
            errors.append(f"{rel}: front matter key 'tools' must be a list of strings")

    return errors, data


def check_templates() -> list[str]:
    """Validate every agent and prompt template, including prompt -> agent links."""
    errors: list[str] = []
    agent_names: dict[str, Path] = {}

    agent_files = sorted(AGENT_DIR.glob("*.agent.md"))
    prompt_files = sorted(PROMPT_DIR.glob("*.prompt.md"))

    if not agent_files:
        errors.append(f"{AGENT_DIR.relative_to(REPO_ROOT)}: no '*.agent.md' templates found")
    if not prompt_files:
        errors.append(f"{PROMPT_DIR.relative_to(REPO_ROOT)}: no '*.prompt.md' templates found")

    for path in agent_files:
        file_errors, data = check_front_matter(path, AGENT_REQUIRED_KEYS)
        errors.extend(file_errors)
        name = data.get("name")
        if isinstance(name, str) and name.strip():
            if name in agent_names:
                other = agent_names[name].relative_to(REPO_ROOT)
                errors.append(
                    f"{path.relative_to(REPO_ROOT)}: agent name '{name}' is already used by {other}"
                )
            else:
                agent_names[name] = path

    for path in prompt_files:
        file_errors, data = check_front_matter(path, PROMPT_REQUIRED_KEYS)
        errors.extend(file_errors)
        agent = data.get("agent")
        if isinstance(agent, str) and agent.strip() and agent not in agent_names:
            known = ", ".join(sorted(agent_names)) or "none"
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: front matter 'agent: {agent}' does not match any "
                f"agent defined in .github/agents (known agents: {known})"
            )

    print(
        f"  checked {len(agent_files)} agent template(s) "
        f"and {len(prompt_files)} prompt template(s)"
    )
    return errors


def strip_code_fences(text: str) -> list[tuple[int, str]]:
    """Return (line number, line) pairs with fenced code blocks removed."""
    kept: list[tuple[int, str]] = []
    in_fence = False
    for number, line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            kept.append((number, line))
    return kept


def check_links() -> list[str]:
    """Verify that every relative Markdown link target exists on disk."""
    errors: list[str] = []
    checked = 0
    files = markdown_files()
    scanned = 0

    for path in files:
        rel = path.relative_to(REPO_ROOT)
        if rel.as_posix() in VENDORED_DOCS:
            continue

        scanned += 1
        for number, line in strip_code_fences(path.read_text(encoding="utf-8")):
            for raw_target in LINK_RE.findall(line):
                target = raw_target.strip().strip("<>")
                if not target or target.startswith(SKIPPED_SCHEMES) or "://" in target:
                    continue

                target = target.split("#", 1)[0]
                if not target:
                    continue

                decoded = unquote(target)
                base = REPO_ROOT if decoded.startswith("/") else path.parent
                resolved = base / decoded.lstrip("/")

                checked += 1
                if not resolved.exists():
                    errors.append(f"{rel}:{number}: link target does not exist -> {raw_target}")

    print(
        f"  checked {checked} relative link(s) across {scanned} Markdown file(s) "
        f"({len(files) - scanned} vendored file(s) skipped)"
    )
    return errors


def main() -> int:
    print("Validating agent and prompt templates...")
    errors = check_templates()

    print("Validating relative Markdown links...")
    errors.extend(check_links())

    sys.stdout.flush()

    if errors:
        print(f"\nFAILED: {len(errors)} problem(s) found\n", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print("\nOK: all documentation and template checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
