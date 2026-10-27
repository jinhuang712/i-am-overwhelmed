# 📦 Install

[English](INSTALL.md) · [简体中文](INSTALL.zh-CN.md)

## Claude Code

Paste this to Claude Code:

```text
Install the plugin from github.com/jinhuang712/i-am-overwhelmed:
claude plugin marketplace add jinhuang712/i-am-overwhelmed
claude plugin install i-am-overwhelmed@i-am-overwhelmed
```

Or run those two commands yourself. Restart Claude Code. It turns on by itself.

⚠️ It replaces any output style you picked, such as Explanatory, because Claude Code allows one at a time. To go back, run `claude plugin disable i-am-overwhelmed@i-am-overwhelmed`.

## Codex

Paste this to Codex:

```text
Append the contents of https://raw.githubusercontent.com/jinhuang712/i-am-overwhelmed/master/codex/AGENTS.md to ~/.codex/AGENTS.md, then tell me to start a new session.
```

If you have `~/.codex/AGENTS.override.md`, Codex reads that instead of `AGENTS.md`, so add the rules there. To remove, delete the appended section.
