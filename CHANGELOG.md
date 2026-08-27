# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Versions 0.1.0 and 0.1.1 are reconstructed from the Git history. They were never
tagged, so no comparison links are given for them.

## [Unreleased]

### Added

- MIT `LICENSE`, referenced from `README.md`.
- `AGENTS.md` describing what this repository is, how the templates relate to
  each other and the conventions to follow when changing them.
- This changelog.
- `.github/workflows/ci.yml`, running Markdown linting plus template and link
  validation on every push to `main` and every pull request.
- `.github/workflows/release.yml`, publishing a GitHub Release from a `v*` tag
  using the matching section of this changelog as the release notes.
- `.github/dependabot.yml`, checking GitHub Actions versions weekly.
- `scripts/validate_docs.py`, which checks that agent and prompt front matter
  parses, that each prompt references an agent that exists, and that every
  relative Markdown link resolves.
- `scripts/extract_release_notes.py`, which turns a changelog section into
  release notes.
- `.markdownlint-cli2.jsonc` with the lint configuration used locally and in CI.

### Fixed

- `README.md` linked to `.github/agents/agent-improvement.agent.md` and
  `.github/prompts/improve-agent.prompt.md`, neither of which exists. The files
  are `refinement.agent.md` and `refine-agent.prompt.md`.
- `README.md` documented the VS Code slash command as `/improve-agent`; the
  prompt is registered as `/refine-agent`.
- `Copilot Prompt/Prompt.md` linked to a non-existent
  `declarative agent instructions.md`. It now points at the copy of the article
  that ships in the same folder.
- A list in `.github/prompts/generate-manifest.prompt.md` was not surrounded by
  blank lines, so it did not render as a list.

### Changed

- Padded Markdown table delimiter rows across the repository so tables satisfy
  the `MD060` lint rule.
- Replaced the vague licensing note in `README.md` with a pointer to `LICENSE`,
  and replaced the manual "Last Updated" footer with a pointer to this
  changelog.

## [0.1.1] - 2025-12-18

### Changed

- Updated the tools list in `.github/agents/refinement.agent.md` to align with
  best practices.

## [0.1.0] - 2025-12-09

### Added

- Initial Agent Builder Refinement toolkit, offering four ways to refine
  declarative agent instructions: a one-shot prompt for Microsoft 365 Copilot
  Chat, a Copilot Studio Light agent configuration, a VS Code custom agent and a
  VS Code prompt file.
- Declarative agent manifest generator for VS Code
  (`.github/agents/generate-agent-manifest.agent.md` and
  `.github/prompts/generate-manifest.prompt.md`), targeting schema v1.6.
- Local copies of the Microsoft Learn article "Write effective instructions for
  declarative agents", for upload as agent knowledge files.
- `.gitignore` covering macOS, Windows, VS Code, Node, Python, log, temporary
  and editor artifacts.
- Introductory header in `Copilot Prompt/Prompt.md`.

### Changed

- Expanded the README files with clearer formatting and usage instructions.

### Removed

- Committed `.DS_Store` files.
