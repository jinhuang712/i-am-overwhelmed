# 😵‍💫 i-am-overwhelmed（我过载了）

[English](README.md) · [简体中文](README.zh-CN.md)

**一套不让你过载的回复规则**

![license](https://img.shields.io/badge/license-MIT-green) ![version](https://img.shields.io/github/v/tag/jinhuang712/i-am-overwhelmed?label=version)

## 👀 看效果

真实输出，同一个提示，分别关掉和打开插件。完整，没有删减。原始文件在 [`examples/`](examples/)。

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

> ## 结论：进程内字典 ✅
>
> 100 人用的内部工具，先用进程内缓存。
>
> ### 为什么
> - **零运维**：不用部署、监控、维护 Redis
> - **更快**：无网络往返
> - **够用**：数据量和并发都很小
>
> ### 什么时候改用 Redis
> | 情况 | 原因 |
> |---|---|
> | 多进程/多实例部署 | 各进程缓存不一致 |
> | 重启后不能冷启动 | 字典随进程丢失 |
> | 缓存需要跨服务共享 | 字典是私有的 |
> | 数据量大到占内存 | 受进程内存限制 |
>
> ### 实现建议
> - 别直接用裸 `dict`，加 **TTL** 和 **大小上限**
>   - Python：`cachetools.TTLCache`，或 `functools.lru_cache`
> - 注意**多线程**下加锁（`TTLCache` 本身不是线程安全的）
> - 写好缓存的**失效逻辑**，这比选存储更容易出 bug
>
> ### 我的猜测
> 我不知道你的语言、部署方式（单进程还是多 worker，比如 gunicorn 多个 worker 就是多进程）。如果是多 worker，进程内缓存会各存一份，需要你确认是否能接受。
>
> ### 问题
> 你的工具是单进程部署，还是多 worker / 多实例？
>
> A. 单进程：直接用进程内缓存（推荐，最简单）
> B. 多 worker 但能容忍短暂不一致：仍用进程内缓存，TTL 设短一点
> C. 多实例且必须一致：用 Redis

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

> ## ✅ 已修复 `test_retry` 的不稳定
>
> **根因:** `tests/test_retry.py` 里断言总耗时 `< 0.03s`。`call_with_retry` 的随机抖动最多会休眠 0.02 + 0.04 = 0.06s,所以偶尔会超时失败。这是测试写错了,`retry.py` 没有问题。
>
> **改动(只改了 `tests/test_retry.py`):**
> - 用 `mock.patch("retry.time.sleep")` 替掉真实休眠,测试不再依赖时间。
> - 不再断言耗时,改为断言休眠恰好 2 次,且延迟分别在 `[0, 0.02]` 和 `[0, 0.04]` 内,这才是代码真正的约定。
> - `test_gives_up` 同样 mock 了 sleep,不再白等。
>
> **验证:** 连续跑 200 次,0 次失败。每次运行不到 0.001 秒。
>
> **没验证的:** 我没看到 CI 配置(仓库里没有 workflow 文件),所以不确定 CI 红是不是只有这一个原因。你可以推一次,看是否变绿。
>
> 我没有提交,改动还在工作区。

### 到底变了什么

| | 关闭 | 打开 |
|---|---|---|
| 结论 | 在第一句 | 第一句，单独成行，带标题和 ✅ |
| 结构 | 段落加要点 | 标题、短要点、表格 |
| 不确定的地方 | 混在正文里 | 单独标出：「我的猜测」「没验证的」 |
| 提问 | 通常没有 | 有问题时放最后，选项 A / B / C，有推荐 |
| 正确性 | 不错 | 不错。不是更聪明，只是更好读。 |

每个提示只跑了一次，所以这些是样本。再跑 20 次的结果（包括一次失误）见 [`examples/README.md`](examples/README.md)。

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
