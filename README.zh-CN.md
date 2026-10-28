# 😵‍💫 i-am-overwhelmed（我过载了）

[English](README.md) · [简体中文](README.zh-CN.md)

**一套不让你过载的回复规则**

![license](https://img.shields.io/badge/license-MIT-green) ![version](https://img.shields.io/github/v/tag/jinhuang712/i-am-overwhelmed?label=version)

## 📦 安装

把下面这段粘贴给 Claude Code：

```text
Install the plugin from github.com/jinhuang712/i-am-overwhelmed:
claude plugin marketplace add jinhuang712/i-am-overwhelmed
claude plugin install i-am-overwhelmed@i-am-overwhelmed
```

或者把这段粘贴给 Codex：

```text
把 https://raw.githubusercontent.com/jinhuang712/i-am-overwhelmed/master/codex/AGENTS.md 的内容追加到 ~/.codex/AGENTS.md，然后提醒我开一个新会话。
```

细节、注意事项和卸载方法见 [INSTALL.zh-CN.md](INSTALL.zh-CN.md)。

## 👀 看效果

真实输出，同一个提示，分别关掉和打开插件。完整，没有删减。全部用 Sonnet 5.5（`claude-sonnet-5-5`）跑的，打开插件的那组用的是插件 0.1.7。原始文件在 [`examples/`](examples/)。

### 「我给一个 100 人用的内部小工具加缓存，用 Redis 还是进程内的字典？」

**Off**

> 用进程内字典（或 `functools.lru_cache` / `cachetools.TTLCache` 这类带过期的封装）就够了。
>
> **理由：**
> - 100 人的规模，数据量和并发都很小，进程内缓存的延迟最低（无网络往返），也不用多维护一个服务。
> - Redis 意味着多一个要部署、监控、处理连接失败和序列化的组件，对内部小工具来说是纯增加的运维成本。
>
> **需要注意的点：**
> - 设置 TTL 和最大容量（例如 `TTLCache(maxsize=1000, ttl=300)`），避免内存无限增长和数据过期不更新。
> - 缓存是每个进程独立的。如果你用 gunicorn 开多个 worker 或多实例部署，各自缓存不共享，命中率会下降，并且可能短时间内读到不一致的数据。对小工具通常可以接受；如果不行，先把 worker 数降到 1–2。
> - 重启即丢失缓存，所以别把它当持久存储。
> - 多线程下，普通 dict 的单次读写是安全的，但"检查再写入"不是原子的；用 `cachetools` 时配合一个 `threading.Lock`。
>
> **什么时候该换 Redis：**
> - 多实例部署且必须共享缓存或保证一致性（比如要做主动失效）。
> - 缓存的计算很昂贵，不能容忍重启后冷启动。
> - 需要跨进程的限流、会话、锁等功能。
> - 项目里本来就已经有 Redis 在跑，那么顺手用也行。
>
> 建议先用进程内缓存，把缓存逻辑封装在一个小函数或类后面，以后真需要时再换成 Redis，改动范围很小。

**On**

> ## 👉 用进程内缓存
>
> 100 人的内部工具，进程内缓存足够了 ✅
>
> - **零运维**：不用部署、监控 Redis，也不用处理连接失败
> - **更快**：没有网络往返
> - **够用**：100 人的数据量，内存几乎不是问题
>
> ## ⚠️ 别直接用裸 `dict`
>
> - **要有 TTL**：否则数据会过期不了
> - **要有大小上限**：否则内存会一直涨
> - **并发要安全**：多线程时注意加锁
>
> 💡 Python 的话，用 `cachetools.TTLCache`（或 `functools.lru_cache`，但它没有 TTL）。别自己手写。
>
> ## 🤔 什么时候该换 Redis
>
> - 跑了**多个进程或实例**（gunicorn 多 worker、多个 pod），而且缓存必须**一致**
> - 重启后**不能接受冷缓存**（比如重建很贵）
> - 需要**主动失效**，且要跨实例生效
>
> 注意：多 worker 时每个进程各有一份缓存，只是命中率低一点，数据可能短时间不一致。如果能接受几十秒到几分钟的陈旧，也不用 Redis。
>
> ## ❓ 问题
>
> 你的工具是单进程还是多实例部署？缓存的数据能容忍多久的陈旧？
>
> - A. 单进程，或多实例但能容忍短时间不一致：用 `TTLCache`。✅ 推荐，最省事
> - B. 多实例，且要求缓存强一致或可主动失效：上 Redis

### 「CI 红了，因为 test_retry 时不时失败。把 CI 弄绿。」

这一次 agent 有工具，真的去修一个偶发失败的测试。**两个版本修得一样对**：mock 掉 sleep，保留有意义的断言，什么都没跳过。差别在汇报。

**Off**

> `test_retry` 现在稳定了:修改后连续跑 30 次全部通过。我没有看 CI 本身,也没有提交。
>
> **原因**:`call_with_retry` 的退避带随机抖动,两次重试的睡眠上限分别是 0.02 秒和 0.04 秒。`test_retry` 却断言总耗时小于 0.03 秒,所以随机到较长的睡眠时就会失败。
>
> **修改**:只改了 `tests/test_retry.py`。
> - 用 `mock` 把 `time.sleep` 和 `random.uniform` 打桩,测试不再依赖真实时间。
> - 把时间断言换成对退避上限的检查:两次的上限依次是 `(0, 0.02)` 和 `(0, 0.04)`,并确认 sleep 被调用了 2 次。
> - `test_gives_up` 同样给 sleep 打桩,免得白白睡眠。
>
> `retry.py` 没动,因为行为本身没问题,是测试的断言有错。
>
> 仓库里提交了 `__pycache__/*.pyc`,跑测试后它们也变成了已修改。你可能想把它们移出版本控制并加进 `.gitignore`,我没有动。

**On**

> 🎉 CI 应该绿了：修完后连跑 200 次，全部通过（修之前 20 次里有 10 次失败）。
>
> ## 原因
> `test_retry` 断言重试总耗时 `< 0.03s`，但 [./retry.py](/private/tmp/claude-501/-Users-jin-huang-dev-projects-i-am-overwhelmed/ad842afa-f550-4cfd-b1a9-dce5446f54db/scratchpad/work-fix-test-zh-on.md/retry.py) 里的 sleep 带随机抖动。两次重试的 sleep 上限合计是 0.02 + 0.04 = 0.06s，所以测试本来就会随机失败。这是测试写错了，代码没问题。
>
> ## 改动
> 只改了 [./tests/test_retry.py](/private/tmp/claude-501/-Users-jin-huang-dev-projects-i-am-overwhelmed/ad842afa-f550-4cfd-b1a9-dce5446f54db/scratchpad/work-fix-test-zh-on.md/tests/test_retry.py)：
> - `test_retry`：mock 掉 `time.sleep`，不再断言耗时。改为断言 sleep 恰好调用 2 次，且每次的值落在退避上限内（0~0.02、0~0.04）。
> - `test_gives_up`：也 mock 了 sleep，测试不再真的睡觉，变快了。
>
> 没有放宽阈值，也没有加重试或 skip。退避逻辑现在是被确定性地检查，而不是碰运气。
>
> ## 顺带发现，没改 ⚠️
> `call_with_retry` 在最后一次失败之后还会 sleep 一次，然后才抛异常。这次睡眠没有意义，白白增加延迟。这是行为改动，所以我没动。要的话一行就能修。
>
> 另外，这个目录不是 git 仓库，我没法看 CI 配置，也没法确认 CI 的 Python 版本和本地一致。

### 到底变了什么

| | 关闭 | 打开 |
|---|---|---|
| 结论 | 在第一句 | 第一句，单独成行，带标题和 ✅ 或 🎉 |
| 结构 | 段落加要点 | 标题、短要点、表格 |
| 不确定的地方 | 混在正文里 | 单独标出：⚠️ 警告、🤔 存疑、💡 提示 |
| 态度 | 只在字里行间 | 也体现在表情符号上，比如 🤔 表示存疑 |
| 提问 | 通常没有 | 有问题时放最后，选项 A / B / C，有推荐 |
| 正确性 | 不错 | 不错。不是更聪明，只是更好读。 |

每个提示只跑了一次，所以这些是样本。再跑 20 次的结果（包括一次失误）见 [`examples/README.md`](examples/README.md)。

## 📏 规则

| | |
|---|---|
| 😴 **关于我** | 假设我很累、在同时做几件事、只想扫一眼，并且想听你的看法。 |
| 🤝 **诚实** | 藏着问题比问题本身更糟。不作弊让东西通过。猜的时候说出来。有异议就反驳。 |
| 💬 **回复** | 总结做过的事。要么简单，要么详细。每个编号旁边写上标题。 |
| 🎨 **格式** | 标题、表格、代码块。表情符号有固定含义。文件用链接，URL 两侧加空格，用引用代码代替行号，小改动用 `diff` 块。 |
| ❓ **提问** | 不弹提问框。有问题放最后问，选项 A / B，带推荐。 |

每个工具一个文件（英文原文）。Claude Code 用 [`plugin/output-styles/i-am-overwhelmed.md`](plugin/output-styles/i-am-overwhelmed.md)，它是插件的输出风格，带 `force-for-plugin` 和 `keep-coding-instructions`，所以压缩上下文后依然有效，也保留了 Claude Code 自己的指令。Codex 用 [`codex/AGENTS.md`](codex/AGENTS.md)，规则相同，去掉了 Claude Code 专属的部分。

这是我自己的偏好。Fork 一份，写你自己的。🍴

## 🔧 调整

改上面那个文件，然后：

- **本地路径安装**（`claude plugin marketplace add /path/to/i-am-overwhelmed`）：运行 `/reload-plugins`。
- **GitHub 安装**：推送，在 `plugin/.claude-plugin/plugin.json` 里升版本号，运行 `claude plugin update i-am-overwhelmed@i-am-overwhelmed`。

## 📚 参考文献

上面规则的背景阅读，不是证明：这些研究都没有测过聊天回复，所以每条规则都是从网页、实验室任务和临床交接推过来的。

- Lim & Dinges (2010), [A meta-analysis of the impact of short-term sleep deprivation on cognitive variables](https://pmc.ncbi.nlm.nih.gov/articles/PMC3290659)
- Cowan (2001), [The magical number 4 in short-term memory](https://pubmed.ncbi.nlm.nih.gov/11515286/)
- Morkes & Nielsen (1997), [Concise, scannable, and objective: how to write for the web](https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/)
- Pernice (2019), [Text scanning patterns: eyetracking evidence](https://www.nngroup.com/articles/text-scanning-patterns-eyetracking/)
- Kim et al. (2024), ["I'm not sure, but...": examining the impact of large language models' uncertainty expression on user reliance and trust](https://www.arxiv.org/abs/2405.00623)
- Steyvers et al. (2025), [What large language models know and what people think they know](https://arxiv.org/abs/2401.13835)
- Bansal et al. (2021), [Does the whole exceed its parts? The effect of AI explanations on complementary team performance](https://arxiv.org/abs/2006.14779)
- Vasconcelos et al. (2023), [Explanations can reduce overreliance on AI systems during decision-making](https://arxiv.org/abs/2212.06823)
- Sharma et al. (2024), [Towards understanding sycophancy in language models](https://arxiv.org/abs/2310.13548)
- Starmer et al. (2014), I-PASS handoff program, [summary on PSNet](https://psnet.ahrq.gov/issue/changes-medical-errors-after-implementation-handoff-program)

## 许可

[MIT](LICENSE)

如果它帮你少翻了一屏文字墙，点个 Star ⭐。
