# Repository guide for coding agents

## What this repository is

This repository is a **documentation and template collection**, not a software
project. It distributes prompts, agent configurations and reference material for
building [declarative agents](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-instructions)
for Microsoft 365 Copilot with Copilot Studio Light (Agent Builder).

Everything shipped here is Markdown (plus one PNG and two PDFs). There is:

- **No source code** and no application to run.
- **No package manifest** - no `package.json`, `pyproject.toml`, `Cargo.toml`
  or `go.mod`.
- **No build step.**
- **No unit test suite.**

Do not add a language toolchain, a package manifest, a build system or a test
framework unless the repository actually gains code that needs one. If you are
asked to "run the tests" or "build the project", the honest answer is that
neither exists; run the documentation checks described below instead.

## Layout

```text
agent-builder-refinement/
├── .github/
│   ├── agents/            # VS Code custom agent definitions (*.agent.md)
│   ├── prompts/           # VS Code prompt files (*.prompt.md)
│   ├── workflows/         # CI and release automation
│   └── dependabot.yml     # GitHub Actions update schedule
├── Agent Builder Template/  # Copy-paste config for Copilot Studio Light
├── Copilot Prompt/          # One-shot prompt for M365 Copilot Chat
├── scripts/                 # Repository checks (see below)
├── AGENTS.md
├── CHANGELOG.md
├── LICENSE
└── README.md
```

The repository offers the same capability through several delivery mechanisms.
When you change the substance of the refinement guidance, check whether the
sibling copies need the same change:

| Delivery mechanism | Source of truth |
| --- | --- |
| M365 Copilot Chat | `Copilot Prompt/Prompt.md` |
| Copilot Studio Light | `Agent Builder Template/Agent Refinement Agent - Configuration.md` |
| VS Code custom agent | `.github/agents/refinement.agent.md` |
| VS Code prompt | `.github/prompts/refine-agent.prompt.md` |
| Manifest generation | `.github/agents/generate-agent-manifest.agent.md` |

## Checks

Two checks run in CI (`.github/workflows/ci.yml`). Both are offline and
deterministic. Run them locally before opening a pull request:

```bash
# Markdown lint - the same version CI uses.
npx --yes markdownlint-cli2@0.23.2

# Template front matter and relative link validation.
python3 -m pip install pyyaml   # only dependency, only needed once
python3 scripts/validate_docs.py
```

`scripts/validate_docs.py` verifies that:

1. Every `.github/agents/*.agent.md` file has YAML front matter that parses and
   contains `description` and `name`.
2. Every `.github/prompts/*.prompt.md` file has YAML front matter that parses and
   contains `description`, `name` and `agent`.
3. Each prompt's `agent:` value matches the `name:` of an agent that exists in
   `.github/agents`, and agent names are unique.
4. Every relative Markdown link and image target in the repository resolves to a
   file or directory that exists.

External `http(s)` links are deliberately **not** fetched, so CI never fails
because a third-party site is slow, rate-limiting or temporarily down.

## Conventions

### Agent and prompt front matter

Agent files (`.github/agents/*.agent.md`) use:

```yaml
---
description: One sentence describing what the agent does
name: Pascal_Snake_Case_Name
tools: ['read/readFile', 'search']
---
```

Prompt files (`.github/prompts/*.prompt.md`) use:

```yaml
---
description: One sentence describing what the prompt does
name: kebab-case-name
argument-hint: What the user should paste or type
agent: Pascal_Snake_Case_Name
tools: ['fetch', 'search']
---
```

The prompt `name` becomes the slash command in VS Code Copilot Chat, so
`refine-agent.prompt.md` is invoked as `/refine-agent`. If you rename a prompt or
agent file, update the front matter, the slash command references and every link
in `README.md` in the same change - the link check will fail otherwise.

### Markdown style

- `markdownlint` runs with defaults except `MD013` (line length), which is off.
  Long prose lines are fine; do not hard-wrap paragraphs.
- Table delimiter rows must be padded (`| --- | --- |`, not `|---|---|`) to
  satisfy `MD060`.
- Use relative links between files in this repository, and URL-encode spaces in
  paths (`Copilot%20Prompt/README.md`).

### Vendored reference material

`Agent Builder Template/Write effective instructions for declarative agents.md`
and `Copilot Prompt/Write effective instructions for declarative agents.md` are
verbatim copies of a Microsoft Learn article, kept so they can be uploaded as
agent knowledge files.

**Do not reword, reformat or "fix" these files.** Their relative links point at
other pages on learn.microsoft.com and will never resolve inside this
repository, which is why `scripts/validate_docs.py` skips them for link
checking. If you refresh them, replace them wholesale from the upstream article.

### Changelog

Every user-visible change gets an entry in `CHANGELOG.md` under `## [Unreleased]`,
following [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Releases are
cut by moving the `Unreleased` entries into a new `## [x.y.z] - YYYY-MM-DD`
section and pushing a matching `vx.y.z` tag; `.github/workflows/release.yml` then
publishes a GitHub Release using exactly that section as the notes. A tag with no
matching changelog section fails the release job on purpose.
