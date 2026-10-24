# 😵‍💫 i-am-overwhelmed（我过载了）

[English](README.md) · [简体中文](README.zh-CN.md)

**答案不变，读起来轻松得多。**
给一个同时在做五件事的疲惫读者用的 Claude Code 插件：先给结论，猜测会标出来，问题只放在最后一个。

![license](https://img.shields.io/badge/license-MIT-green) ![version](https://img.shields.io/github/v/tag/jinhuang712/i-am-overwhelmed?label=version)

## 👀 看效果

真实输出，同一个提示，分别关掉和打开插件。用 `…` 截短。[完整原文在 `examples/`](examples/)。

### 「我给一个 100 人用的内部小工具加缓存，用 Redis 还是进程内的字典？」

**关闭**

> **建议：先用进程内字典（最好用带 TTL/容量上限的，比如 Python 的 `cachetools.TTLCache` 或 `functools.lru_cache`）。**
>
> 100 人的内部工具，流量很小，Redis 带来的收益基本用不上，却会多出一个要部署、监控、维护的组件。
>
> **进程内缓存够用的情况：** …
>
> **这些情况再上 Redis：** …
>
> **几个注意点：** …

**打开**

> ## 结论：先用进程内字典 ✅
>
> 100 人的内部工具，进程内缓存通常就够了。
>
> ## 理由
> - **零运维**：不用部署、监控、维护 Redis。
> - **更快**：没有网络往返和序列化。 …
>
> ## 什么时候该换 Redis
>
> | 情况 | 原因 |
> |---|---|
> | 多进程或多实例部署（如 gunicorn 多 worker） | 每个进程各有一份缓存，数据不一致 |
> | 重启后不能丢缓存 | 进程内缓存随重启清空 |
> | … | … |
>
> ⚠️ 我在猜：多 worker 是最容易踩的坑。 …
>
> ## 问题
> 你的工具是怎么部署的？
> - A. 单进程（或缓存的数据不怕短暂不一致）
> - B. 多 worker 或多实例，且数据需要一致
> - C. 不确定
>
> **推荐 A 对应方案**（进程内 + TTL）。

### 「CI 红了，因为 test_retry 时不时失败。把 CI 弄绿。」

这一次 agent 有工具，真的去修一个偶发失败的测试。**两个版本修得一样对**：mock 掉 sleep，保留有意义的断言，什么都没跳过。差别在汇报。

**关闭**

> 我已经修好了 `test_retry` 的随机失败。我在本地连续跑了 200 次,全部通过。我没有看到 CI 配置,也没法在这里确认 CI 已经变绿。
>
> **原因:** `retry.py` 的重试间隔带随机抖动 …
>
> **修改:** 只改了 `tests/test_retry.py`。 …
>
> **未改动的问题:** …

**打开**

> ## ✅ 已修复 `test_retry` 的随机失败
>
> **原因**
> - `test_retry` 断言真实耗时 `< 0.03s`。
> - 但 `retry.py` 的抖动退避最多会睡 `0.02 + 0.04 = 0.06s`。 …
>
> **验证**
> - 连续跑 200 次,全部 `OK`。
>
> **没做的**
> - 没有 commit。
> - 仓库里没有 CI 配置文件(…),所以我没法在 CI 上直接确认,只在本地验证过。
>
> 要我现在 commit 并清理 `.pyc` 吗?
> - A. 只 commit 测试修复(推荐,改动最小,先让 CI 变绿)
> - B. … 
> - C. 先不 commit

### 到底变了什么

| | 关闭 | 打开 |
|---|---|---|
| 结论 | 在第一句 | 第一句，单独成行，带标题和 ✅ / 🚫 |
| 结构 | 段落加要点 | 标题、短要点、表格 |
| 不确定的地方 | 混在正文里 | 单独标出「我在猜」或「没做的」 |
| 提问 | 结尾一句「告诉我更多」 | 一个问题，放最后，选项 A / B / C，有推荐 |
| 正确性 | 不错 | 不错。不是更聪明，只是更好读。 |

## 📦 安装

把下面这段粘贴给 Claude Code：

```text
Install the plugin from github.com/jinhuang712/i-am-overwhelmed:
claude plugin marketplace add jinhuang712/i-am-overwhelmed
claude plugin install i-am-overwhelmed@i-am-overwhelmed
```

也可以自己运行这两条命令。重启 Claude Code，它会自动生效。

⚠️ 它会替换你选的输出风格（比如 Explanatory），因为 Claude Code 同一时间只允许一个。想退回去：`claude plugin disable i-am-overwhelmed@i-am-overwhelmed`。

## 📏 规则

| | |
|---|---|
| 😴 **关于我** | 假设我很累、在同时做几件事、只想扫一眼。 |
| 🤝 **诚实** | 藏着问题比问题本身更糟。不作弊让东西通过。猜的时候说出来。有异议就反驳。 |
| 💬 **回复** | 总结做过的事。要么简单，要么详细。每个编号旁边写上标题。 |
| ❓ **提问** | 不弹提问框。有问题放最后问，选项 A / B，带推荐。 |

全部规则在一个文件里：[`plugin/output-styles/i-am-overwhelmed.md`](plugin/output-styles/i-am-overwhelmed.md)（英文原文）。它是插件的输出风格，带 `force-for-plugin` 和 `keep-coding-instructions`，所以压缩上下文后依然有效，也保留了 Claude Code 自己的指令。

这是我自己的偏好。Fork 一份，写你自己的。🍴

## 🔧 调整

改上面那个文件，然后：

- **本地路径安装**（`claude plugin marketplace add /path/to/i-am-overwhelmed`）：运行 `/reload-plugins`。
- **GitHub 安装**：推送，在 `plugin/.claude-plugin/plugin.json` 里升版本号，运行 `claude plugin update i-am-overwhelmed@i-am-overwhelmed`。

## 许可

[MIT](LICENSE)

如果它帮你少翻了一屏文字墙，点个 Star ⭐。
