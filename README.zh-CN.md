# 😵‍💫 i-am-overwhelmed（我过载了）

[English](README.md) · [简体中文](README.zh-CN.md)

**一套不让你过载的回复规则**

![license](https://img.shields.io/badge/license-MIT-green) ![version](https://img.shields.io/github/v/tag/jinhuang712/i-am-overwhelmed?label=version)

## 📦 安装

**给 Claude Code 安装**

1. 用命令行：

```bash
claude plugin marketplace add jinhuang712/i-am-overwhelmed
claude plugin install i-am-overwhelmed@i-am-overwhelmed
```

2. 用 curl：

```bash
curl -fsSL https://raw.githubusercontent.com/jinhuang712/i-am-overwhelmed/master/install-claude.sh | sh
```

**让 agent 来安装**

把这句话贴给 Claude Code、Codex 或其他 agent：

```text
Install i-am-overwhelmed by following https://raw.githubusercontent.com/jinhuang712/i-am-overwhelmed/master/INSTALL.md
```

细节、注意事项和卸载方法见 [INSTALL.zh-CN.md](INSTALL.zh-CN.md)。

## 👀 看效果

真实输出，同一个提示，分别关掉和打开插件。完整，没有删减。全部用 Sonnet 5.5（`claude-sonnet-5-5`）跑的，打开插件的那组录于 2026-11-10，用的是本仓库当前的规则。点开 **关闭** 可以看不带插件的回复。原始文件在 [`examples/`](examples/)。

### 「我给一个 100 人用的内部小工具加缓存，用 Redis 还是进程内的字典？」

<details>
<summary><b>关闭</b>（15 行）</summary>

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

</details>

**打开**（14 行）

> 我的意见：**先用进程内字典** ✅ 100 人的量，Redis 多出来的是一个要部署、监控、维护的服务，收益很小。
>
> ```
> 缓存放哪里？
> ├── 单进程部署
> │   → 进程内字典（加 TTL 和大小上限）
> ├── 多进程或多实例，且能接受数据短暂不一致
> │   → 还是进程内字典，TTL 设短一点
> └── 多实例，且要求数据强一致或要共享
>     → 这时才上 Redis
> ```
>
> - 💡 **别手写 dict**：Python 用 `cachetools.TTLCache`，Node 用 `lru-cache`，这样过期和内存上限都自带。
> - ⚠️ **重启即清空**：进程内缓存随进程消失，重启后第一批请求会慢一点，内部工具通常无所谓。
> - 🤔 **我在猜的部分**：我不知道你的部署方式。多 worker（比如 gunicorn 开 4 个进程）时，每个进程各有一份缓存，数据可能不一致。
>
> Q1. 这个工具跑几个进程？（几个字回答即可，例如"单进程"或"gunicorn 4 个 worker"）

### 「用户在我们的网站上点『用 GitHub 登录』之后，浏览器、我们的后端和 GitHub 之间是怎么一步步交互的？」

<details>
<summary><b>关闭</b>（47 行）</summary>

> 这是标准的 OAuth 2.0 授权码流程（Authorization Code Flow）。
>
> ## 时序
>
> ```
> 浏览器                    我们的后端                    GitHub
>   |  1. 点「用 GitHub 登录」  |                            |
>   |------------------------->|                            |
>   |                          | 生成 state（可选 PKCE）存 session
>   |  2. 302 到 GitHub 授权页  |                            |
>   |<-------------------------|                            |
>   |  3. GET /login/oauth/authorize?client_id&redirect_uri&scope&state
>   |------------------------------------------------------>|
>   |  4. 用户登录 GitHub（如未登录）并点「Authorize」          |
>   |<----------------------------------------------------->|
>   |  5. 302 到 redirect_uri?code=xxx&state=yyy             |
>   |<------------------------------------------------------|
>   |  6. GET /auth/github/callback?code&state              |
>   |------------------------->|                            |
>   |                          | 7. 校验 state 与 session 中一致
>   |                          | 8. POST /login/oauth/access_token
>   |                          |    (client_id, client_secret, code, redirect_uri)
>   |                          |--------------------------->|
>   |                          |    access_token            |
>   |                          |<---------------------------|
>   |                          | 9. GET api.github.com/user
>   |                          |    Authorization: Bearer <token>
>   |                          |--------------------------->|
>   |                          |    id, login, avatar...    |
>   |                          |<---------------------------|
>   |                          | 10. 查找/创建本地用户，建立会话
>   | 11. Set-Cookie: session + 302 到首页                    |
>   |<-------------------------|                            |
> ```
>
> ## 各步骤要点
>
> 1. **发起**：后端生成随机 `state`（防 CSRF），存进 session 或签名 cookie。如果用 PKCE，同时生成 `code_verifier` 并把 `code_challenge` 带上。
> 2. **跳转授权页**：参数有 `client_id`、`redirect_uri`、`scope`（只要登录用 `read:user`，要邮箱再加 `user:email`）和 `state`。
> 3. **用户授权**：这一步完全发生在浏览器和 GitHub 之间，我们的后端看不到。
> 4. **回调**：GitHub 把用户重定向回我们预先注册的 `redirect_uri`，带上一次性的 `code`（短时效，约 10 分钟）和原样返回的 `state`。
> 5. **校验 state**：不一致就直接拒绝，这是防登录 CSRF 的关键。
> 6. **换 token**：后端用 `code` + `client_secret` 向 GitHub 请求 `access_token`。这一步是服务器对服务器，`client_secret` 不会暴露给浏览器。请求时加 `Accept: application/json`，否则 GitHub 默认返回 form 编码格式。
> 7. **取用户信息**：用 token 调 `GET /user`。如果需要邮箱，再调 `GET /user/emails`，因为用户可能把邮箱设为私密，`/user` 里的 `email` 可能为空。
> 8. **建立本地会话**：用 GitHub 的**数字 `id`** 作为唯一标识去匹配或创建本地用户，不要用 `login`（可改名）或 email。然后下发自己的会话 cookie（`HttpOnly; Secure; SameSite=Lax`）。
>
> ## 容易踩的点
>
> - `access_token` 只留在后端。如果只用来登录，用完就可以丢掉，不必存。
> - `redirect_uri` 必须和 GitHub OAuth App 中注册的一致，否则授权会失败。
> - `code` 只能用一次。
> - 登录之后浏览器和 GitHub 就没关系了，后续请求只带我们自己的 session cookie。
>
> 如果你想对照项目里的实际实现来检查（比如 state 校验、用什么字段做用户唯一标识），告诉我代码在哪，我可以帮你看。

</details>

**打开**（29 行）

> 我假设你们用的是标准的 OAuth 2.0 授权码流程（authorization code flow，先拿一次性 code，再换 token），我没看你们的代码，所以这是推测。
>
> ```
> 浏览器        我们的后端        GitHub
>   │ 1 点「用 GitHub 登录」 │
>   ├──────────▶│
>   │ 2 302 跳转到 GitHub    │
>   │◀──────────┤  (带 client_id, redirect_uri, scope, state)
>   │ 3 跳去 GitHub，用户登录并点「授权」
>   ├───────────────────────▶│
>   │ 4 302 回到我们的回调地址
>   │◀───────────────────────┤  (带 code, state)
>   │ 5 浏览器访问回调地址
>   ├──────────▶│
>   │           │ 6 用 code + client_secret 换 token
>   │           ├───────────▶│
>   │           │ 7 返回 access_token
>   │           │◀───────────┤
>   │           │ 8 用 token 调 GET /user 拿用户信息
>   │           ├───────────▶│
>   │ 9 建立登录态 (Set-Cookie)
>   │◀──────────┤
> ```
>
> - **前台通道**（1-5）：走浏览器，所有内容用户都看得到，所以只放 `code`（一次性授权码），不放密钥。
> - **后台通道**（6-8）：后端直连 GitHub，`client_secret` 和 `access_token` 只在这里出现。
> - **`state`**：后端在第 2 步生成的随机串，第 5 步必须核对一致，用来防 CSRF（跨站请求伪造）。
>
> ❗ 最常见的坑：漏掉 `state` 校验，或把 `client_secret` 放进前端。
>
> Q1. 你想接着深入哪一块？（快问快答）
> - 我推荐先讲 `state` 校验的实现，因为它最容易漏，也最容易出安全问题。
> - 或者讲 token 换到之后，怎么和你们自己的用户表绑定。

### 「CI 红了，因为 test_retry 时不时失败。把 CI 弄绿。」

这一次 agent 有工具，真的去修一个偶发失败的测试。**两个版本修得一样对**：mock 掉 sleep，保留有意义的断言，什么都没跳过。差别在汇报。

<details>
<summary><b>关闭</b>（8 行）</summary>

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

</details>

**打开**（19 行）

> 🎉 `test_retry` 修好了，连续跑 200 次全部通过。
>
> **根因**
> ```
> retry.py 睡眠 = random.uniform(0, 0.02 * 2**i)
>   → 两次失败最多睡 0.02 + 0.04 = 0.06s
>   → 测试断言总耗时 < 0.03s
>   → 抖动取到大值就失败
> ```
>
> **改动**：只改了 [./tests/test_retry.py](/tmp/work/tests/test_retry.py)。
> ```diff
> - self.assertLess(time.monotonic() - start, 0.03)
> + # mock sleep，并让 jitter 取上限
> + self.assertEqual([c.args[0] for c in sleep.call_args_list], [0.02, 0.04])
> ```
> `test_gives_up` 也 mock 了 sleep，不再真睡。
>
> - **没有放宽阈值**：我没有把 0.03 改大。新断言检查的是延迟上限，比计时更准，也不依赖机器快慢。
> - **`retry.py` 没动**：生产代码本身是对的。
> - ⚠️ **没验证 CI 本身**：这里没有 CI 配置，也不是 git 仓库。我只在本地用 `PYTHONPATH=. python3 -m unittest tests.test_retry` 跑过。你的 CI 如果用别的命令，比如 pytest，路径设置可能不同。
>
> 下一步：把你的 CI 运行命令发我，我照那个命令再验证一遍。

### 到底变了什么

| | 关闭 | 打开 |
|---|---|---|
| 长度 | 一次全倒出来 | 先给几行，你要了再展开 |
| 结构 | 标题加段落 | 内容有形状就画图，否则用要点 |
| 不确定的地方 | 混在正文里 | 单独标出：⚠️ 警告、🤔 存疑、💡 提示 |
| 只有你知道的事实 | 先假设，再往下推 | 先问你 |
| 提问 | 通常没有 | 放最后，用固定题型；要你做决定时带推荐 |
| 正确性 | 不错 | 不错。不是更聪明，只是更好读。 |

每个提示只跑了一次，所以这些是样本。它们是怎么录的，以及更早的 20 次运行的结果（包括一次失误），见 [`examples/README.md`](examples/README.md)。

## 📏 规则

| | |
|---|---|
| 😴 **关于我** | 假设我很累、同时做几件事、只想扫一眼、想听你的看法，容易丢了大局，而且看图比看列表快。 |
| 🤝 **诚实** | 藏着问题比问题本身更糟。猜的时候说出来，也说清你实际验证了什么。不作弊让东西通过。如实汇报做完的工作。 |
| 🔍 **质疑** | 列出你和我的前提，逐条核实，重要的摆出来。只有我才知道的前提，先问我再往下推。有异议就反驳。没被说服就坚持立场。 |
| 💬 **回复** | 默认用简单模式：几行，不带标题。我要求展开，或者简单版会误导我时，才用详细模式：只讲一件事，带标题。只深入讲一件事，多件事就各自简述。一次一件事，并同步全局进度。大局变了，开头用 📍 一行写目标、已定、待定。偏离目标就提醒我。 |
| 🧱 **结构** | 先化简，再给剩下的内容加结构。每条回复都要有结构。内容有形状就画出来：ASCII 树、图、箭头瀑布、思维导图，对比用表格。图的每一层缩进相同。英文的图必须把列对齐。需要对齐的图只用英文；带中文标注的图不做补齐，想对齐就把说明放到下一行。没有形状的内容才用要点，每条只讲一点，写成 `- **关键词**: 说明`。详细模式下，回复的每个部分都有标题，各部分之间加一条 `---`。引用的原文和不需要突出的提醒放进引用块。命令和代码单独放进代码块，改动用 `diff` 块。 |
| ✍️ **用词** | 用正面说法。少用连接词。不用双重否定。不用排比。新词第一次出现就解释。可以加一点幽默。 |
| 🎨 **格式** | 表情符号有固定含义。文件和文件夹用链接，每个编号旁边写上标题，URL 两侧加空格，不写行号。 |
| ❓ **提问** | 不弹提问框。答案清楚就自己定，定完告诉我。一个问题只装一个决定。每条回复以一条出路收尾：需要我回答就提问，否则写下一步。需要问几个就问几个，先解释再问，放在最后，编号为 Q1、Q2。每个问题都用固定题型：选择题（2 到 4 个选项）、多选题、是非题、快问快答或排序题。需要我确认的事一律写成问题。让我做决定的选择题带推荐，理由用要点写在选项下面。 |

大多数规则是一行带标签的短句：`[YES]` 要做，`[NO]` 不要做，`[MAYBE]` 你决定，`[WHEN]` 某种情况（"情况：怎么做"）。

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
