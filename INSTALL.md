# 📦 Install

This page is written for the agent that installs the rules. A person can follow it too.

Claude Code needs its `claude` command and `curl`. Codex or another agent needs a file of global instructions it can edit.

---

## Claude Code

Run this in a terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/jinhuang712/i-am-overwhelmed/master/install-claude.sh | sh
```

[`install-claude.sh`](install-claude.sh) adds the marketplace and installs the plugin. Then it checks that the plugin is installed and enabled, and prints its version. It runs these two commands, which you can also run yourself:

```bash
claude plugin marketplace add jinhuang712/i-am-overwhelmed
claude plugin install i-am-overwhelmed@i-am-overwhelmed
```

Then tell the user to restart Claude Code. The output style turns on by itself.

⚠️ It replaces any output style the user picked, such as Explanatory, because Claude Code allows one at a time.

To check that it worked, now or later, run:

```bash
curl -fsSL https://raw.githubusercontent.com/jinhuang712/i-am-overwhelmed/master/install-claude.sh | sh -s -- --check
```

---

## Codex and other agents

The rules are one file: https://raw.githubusercontent.com/jinhuang712/i-am-overwhelmed/master/codex/AGENTS.md

4 steps:

1. Read that file.
2. Find the user's global instructions. For Codex that is `~/.codex/AGENTS.md`, or `~/.codex/AGENTS.override.md` when it exists, because Codex reads that one instead.
3. Add the rules there. How they fit is your call:
   - Keep the user's own instructions.
   - Replace an older copy of these rules, so the file holds one copy.
   - Tell the user where a rule conflicts with one of theirs.
4. Tell the user to start a new session.

---

## Update

For Claude Code, run the install line again: when the marketplace and the plugin are already there, the script updates them.

For Codex and other agents, do the 4 steps again and replace the older copy.

---

## Remove

For Claude Code, go back to the output style you had with:

```bash
claude plugin disable i-am-overwhelmed@i-am-overwhelmed
```

For Codex and other agents, delete the section with the rules from the file of global instructions.
