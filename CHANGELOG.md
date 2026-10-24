# Changelog

All notable changes to this project are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [0.1.1] - 2026-10-25

### Removed
- The Research and Development sections of the output style. They are work habits, not reply rules, so the plugin now holds reply rules only: about me, honesty, replies and asking. I moved the two sections to my own `~/.claude/CLAUDE.md`.

### Fixed
- The README rules table said "one question". The rule only says that questions go last.

## [0.1.0] - 2026-10-25

First public release.

### Added
- The plugin: my personal preferences, loaded as a forced output style (`plugin/output-styles/i-am-overwhelmed.md`) so they are in the system prompt of every session.
- `README.md` and `README.zh-CN.md`, built on real before-and-after output.
- `examples/`: the raw outputs behind the README, the fixture, and what to know before trusting them.
