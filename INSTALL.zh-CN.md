# 📦 安装

[English](INSTALL.md) · [简体中文](INSTALL.zh-CN.md)

这一页写给负责安装的 agent，人也可以照着做。

## Claude Code

在终端运行：

```bash
curl -fsSL https://raw.githubusercontent.com/jinhuang712/i-am-overwhelmed/master/install-claude.sh | sh
```

[`install-claude.sh`](install-claude.sh) 会添加 marketplace 并安装插件，已经装过就改为更新。然后它会检查插件是否已安装并启用，并打印版本号。它运行的是下面两条命令，你也可以自己运行：

```bash
claude plugin marketplace add jinhuang712/i-am-overwhelmed
claude plugin install i-am-overwhelmed@i-am-overwhelmed
```

以后想检查安装情况，运行：

```bash
curl -fsSL https://raw.githubusercontent.com/jinhuang712/i-am-overwhelmed/master/install-claude.sh | sh -s -- --check
```

然后告诉用户重启 Claude Code，输出风格会自动启用。

⚠️ 它会替换用户已选的输出风格（如 Explanatory），因为 Claude Code 一次只能用一个。想恢复就运行 `claude plugin disable i-am-overwhelmed@i-am-overwhelmed`。

## Codex 和其他 agent

规则只有一个文件： https://raw.githubusercontent.com/jinhuang712/i-am-overwhelmed/master/codex/AGENTS.md

1. 读这个文件。
2. 找到用户的全局指令文件。Codex 是 `~/.codex/AGENTS.md`；如果存在 `~/.codex/AGENTS.override.md`，就用它，因为 Codex 会优先读它。
3. 把规则加进去。怎么放由你判断：
   - 保留用户自己的指令。
   - 文件里已有旧版规则就替换掉，只留一份。
   - 有规则和用户的指令冲突时，告诉用户。
4. 告诉用户新开一个会话。

想移除规则，把那一节从文件里删掉即可。
