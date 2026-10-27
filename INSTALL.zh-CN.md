# 📦 安装

[English](INSTALL.md) · [简体中文](INSTALL.zh-CN.md)

## Claude Code

把下面这段粘贴给 Claude Code：

```text
Install the plugin from github.com/jinhuang712/i-am-overwhelmed:
claude plugin marketplace add jinhuang712/i-am-overwhelmed
claude plugin install i-am-overwhelmed@i-am-overwhelmed
```

也可以自己运行这两条命令。重启 Claude Code，它会自动生效。

⚠️ 它会替换你选的输出风格（比如 Explanatory），因为 Claude Code 同一时间只允许一个。想退回去：`claude plugin disable i-am-overwhelmed@i-am-overwhelmed`。

## Codex

把下面这段粘贴给 Codex：

```text
把 https://raw.githubusercontent.com/jinhuang712/i-am-overwhelmed/master/codex/AGENTS.md 的内容追加到 ~/.codex/AGENTS.md，然后提醒我开一个新会话。
```

如果你有 `~/.codex/AGENTS.override.md`，Codex 会读它而不是 `AGENTS.md`，所以请把规则加到那里。想移除，删掉追加的那一段。
