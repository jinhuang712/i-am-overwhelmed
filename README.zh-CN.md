<img src="assets/hero.zh-CN.svg" alt="我过载了。一位被烦到的用户写给编程 agent 的话，其中的回复规则被划了出来。" width="100%">

# 😵‍💫 i-am-overwhelmed（我过载了）

[English](README.md) · [简体中文](README.zh-CN.md)

**一套不让你过载的回复规则**

![license](https://img.shields.io/badge/license-MIT-green) ![version](https://img.shields.io/github/v/tag/jinhuang712/i-am-overwhelmed?label=version) [![benchmark](https://img.shields.io/badge/benchmark-82.1%20vs%2077.2%20without-blue)](#-基准测试)

你很累，同时在做三件别的事，只想扫一眼。这个插件让 Claude 照着这样的读者来回复。它的回复是：

- **Honest（诚实）**：问题、猜测、没验证的结论，都直接说出来。
- **Simple（简单）**：先给几行，你要了再展开。
- **Structured（有结构）**：内容有形状就画图，否则用要点。
- **Asking（先问）**：只有你知道的事实，先问你，不靠假设。
- **Opinionated（有主见）**：给出看法，有异议就反驳，没被说服就坚持。
- **Focused（聚焦）**：一次只讲一件事，话题偏离目标时会提醒你。
- **Standalone（能单独读懂）**：每条回复都不用往回翻就能看懂。
- **Predictable（可预期）**：每次都是同样的格式、同样的表情含义，你知道该看哪里。

## 🎁 你能得到什么

- **更干净的上下文，更少跑偏**：Claude 打印的每条回复都会成为下一轮的上下文，所以回复短、有结构，长对话就不容易跑偏。
- **少走弯路**：它先问再假设，工作不会建在对你的猜测上。
- **读得更少**：结论在最前面，细节等你要了再给。
- **不会事后才发现**：坏了的、猜的、没验证的，现在就说，不留到以后。

**干活也感觉不一样了。** 这个插件只设置输出风格，规则管的也只是回复。但用上它以后，agent 给人的感觉是这样的：

- **更诚实**：会说清哪些没核实。这一点基准测试也印证了：70% 的回复做到了，不装插件只有 18%。
- **先查再动手**：推理或改东西之前，会先调查。
- **更好奇**：问得更多，也会多想一步。
- **会反驳**：会提出反对意见和更好的方案。
- **先规划，不倒结论**：会主动拆分任务、做规划，而不是一下子倒出一大堆结论。
- **感觉更快**：没那么容易想过头，更快进入状态，也更早抓住重点。

原因我只能猜，因为我看不到模型内部：规则要求回复说出某些东西，比如核实过什么，模型可能就会先把这些做到，才好说出来。

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

## 🧱 它是怎么工作的

**这个插件只设置一样东西：Claude Code 的输出风格（output style）。** 它不加 hook，不加 skill，不加工具，也不写 `CLAUDE.md`。

```
Claude Code
├── system prompt
│   ├── coding instructions    kept as they are
│   └── output style           the one thing this plugin sets
├── CLAUDE.md                  untouched
└── hooks, skills, tools       untouched
```

它的规则管的是 Claude 怎么和你对话，工程上的事留给 Claude Code 自己的指令。它是一组指令，所以大多数回复会照做，但不是每一条。

每个工具一个文件（英文原文）。Claude Code 用 [`plugin/output-styles/i-am-overwhelmed.md`](plugin/output-styles/i-am-overwhelmed.md)，它是插件的输出风格，带 `force-for-plugin` 和 `keep-coding-instructions`，所以压缩上下文后依然有效，也保留了 Claude Code 自己的指令。Codex 用 [`codex/AGENTS.md`](codex/AGENTS.md)，规则相同，去掉了 Claude Code 专属的部分。

为什么这样设计，以及规则为什么这样写，见 [PHILOSOPHY.md](PHILOSOPHY.md)（英文）。

## 👀 看效果

真实输出，同一个提示，分别关掉和打开插件。完整，没有删减。每个示例都取自 2026-11-11 的基准测试，用的是 Claude Opus 5.5（`claude-opus-5-5`）。点开 **关闭** 可以看不带插件的回复。原始文件在 [`examples/`](examples/)。

### 「我们有个内部工具，大约 100 人用。要不要上 Redis 做缓存？」

<details>
<summary><b>关闭</b>（15 行）</summary>

> **大概率不需要。** 100 人规模的内部工具，Redis 带来的运维成本通常高于收益。
>
> ### 为什么一般不需要
> - **负载很低**：100 人就算同时在线，QPS 通常也就几十，PostgreSQL / MySQL 单机就能轻松应对。
> - **增加复杂度**：多一个组件，就要多考虑部署、监控、高可用和缓存一致性。缓存失效导致的数据不一致，在内部工具里很容易引发难查的 bug。
> - **有更简单的替代方案**：
>   - 先优化数据库：加索引、处理慢查询、解决 N+1 问题，这通常是最大的收益点
>   - 使用进程内缓存（如 Python 的 `functools.lru_cache`/`cachetools`、Java 的 Caffeine、Node 的 `lru-cache`），适合单实例部署
>   - 对静态资源和不常变的接口，配置 HTTP 缓存头
>
> ### 什么情况下值得上
> - **已经测出明确瓶颈**：比如某个查询或外部 API 调用很慢（秒级）、很贵，或者有限流。
> - **多实例部署且需要共享状态**：如 session、分布式锁、限流计数，或者用作任务队列（Celery/Sidekiq/BullMQ）。
> - **公司已有托管的 Redis**（云服务或平台组维护），接入成本几乎为零，这时用它也无妨。
>
> ### 建议
> 先看监控或 APM，确认慢在哪里。如果数据库优化后仍有明显瓶颈，再考虑缓存，而且优先用进程内缓存。只有在多实例需要共享缓存，或者用到队列、锁这类功能时，才引入 Redis。
>
> 如果你能说一下现在遇到的具体问题（比如哪个页面慢、技术栈、部署了几个实例），我可以给更有针对性的建议。

</details>

**打开**（24 行）

> 🤔 大概率不用。100 人的内部工具，数据库通常扛得住；Redis 会多一个要部署、监控、处理缓存失效的组件。前提是还没测出具体的慢点。这一条是猜测，我没看到你们的系统。
>
> 先排查，再决定要不要上 Redis：
>
> ```
> 接口慢吗？
> ├── 不慢
> │   → 不上 Redis，保持简单 ✅
> └── 慢
>     ├── 慢在 SQL
>     │   → 先加索引、改查询
>     ├── 慢在调外部 API
>     │   → 先用进程内缓存（如 LRU）
>     └── 以上都试过，或要多实例共享缓存、session
>         → 这时再上 Redis
> ```
>
> 值得上 Redis 的 3 种情况：
>
> - **多实例共享**：你们部署了多个实例，需要共享 session 或缓存。
> - **外部调用贵**：某个外部 API 很慢，或者按调用次数收费。
> - **已经有 Redis**：公司已有托管 Redis，接入几乎没有运维成本。
>
> > 100 人用的工具上 Redis，常常是在给不存在的流量做准备 😄
>
> 💬 现在有没有具体的慢点或痛点？
> - A. 没有，只是想提前优化
> - B. 有，某些接口明显慢
> - C. 有，需要多实例共享状态
>
> 选 A 就不用上 Redis。选 B 或 C，告诉我具体情况，我帮你判断。

### 「用户在我们的网站上点『用 GitHub 登录』之后，浏览器、我们的后端和 GitHub 之间是怎么交互的？」

<details>
<summary><b>关闭</b>（67 行）</summary>

> 这是标准的 **OAuth 2.0 授权码流程（Authorization Code Flow）**。整个过程分为以下几步：
>
> ## 时序概览
>
> ```
> 浏览器                 你的后端                     GitHub
>   |  1. 点击登录          |                            |
>   |--------------------->|                            |
>   |  2. 302 重定向到 GitHub (带 client_id, state...)    |
>   |<---------------------|                            |
>   |  3. 访问 github.com/login/oauth/authorize          |
>   |-------------------------------------------------->|
>   |  4. 用户登录 GitHub 并点击“授权”                     |
>   |  5. 302 重定向回 callback?code=xxx&state=yyy       |
>   |<--------------------------------------------------|
>   |  6. 访问你的 callback  |                            |
>   |--------------------->|  7. 用 code 换 access_token |
>   |                      |--------------------------->|
>   |                      |<---------------------------|
>   |                      |  8. 用 token 拉取用户信息    |
>   |                      |--------------------------->|
>   |                      |<---------------------------|
>   |  9. 建立会话(Set-Cookie)，跳转到站内页面            |
>   |<---------------------|                            |
> ```
>
> ## 各步骤详解
>
> **1–2. 发起授权（浏览器 → 后端）**
> 后端生成一个随机 `state`，存入 session 或 cookie，然后返回 302 重定向到：
> ```
> https://github.com/login/oauth/authorize
>   ?client_id=YOUR_CLIENT_ID
>   &redirect_uri=https://yoursite.com/auth/github/callback
>   &scope=read:user user:email
>   &state=随机字符串
> ```
> - `state` 用于防御 CSRF。
> - 如有需要，还可以加上 PKCE 参数（`code_challenge` / `code_challenge_method=S256`），GitHub 已支持。
>
> **3–4. 用户在 GitHub 上授权**
> 如果用户还没登录 GitHub，会先完成登录。随后 GitHub 展示授权页面，列出你的应用和申请的权限范围。用户此前授权过的话，这一步会自动跳过。
>
> **5–6. 回调（GitHub → 浏览器 → 后端）**
> GitHub 把浏览器重定向到你的 `redirect_uri`，并带上 `?code=一次性授权码&state=原样返回`。
> 后端收到后必须先校验 `state` 与第 1 步保存的一致，不一致就拒绝请求。
>
> **7. 用 code 换 token（后端 ↔ GitHub，服务器之间直连）**
> ```
> POST https://github.com/login/oauth/access_token
> Accept: application/json
>
> client_id=...&client_secret=...&code=...&redirect_uri=...
> ```
> 返回 `access_token`。`client_secret` 只出现在这一步的服务器之间请求里，**绝不能暴露给浏览器**。`code` 只能使用一次，有效期很短（约 10 分钟）。
>
> **8. 获取用户身份**
> ```
> GET https://api.github.com/user
> Authorization: Bearer <access_token>
> ```
> 从返回结果中拿到 `id`、`login`、`avatar_url` 等信息。如果需要邮箱，再调用 `GET /user/emails`，取其中 `primary` 且 `verified` 的那一个。
>
> **9. 建立你自己的登录态**
> - 用 GitHub 的 **`id`**（数字，永久不变）关联或创建本地用户。不要用 `login` 用户名，因为用户可以改名。
> - 签发你自己的 session cookie 或 JWT，然后重定向到首页或用户登录前所在的页面。
> - 如果之后不需要代表用户调用 GitHub API，可以直接丢弃 access_token；如果需要，就加密保存。
>
> ## 关键安全要点
> | 要点 | 原因 |
> |---|---|
> | 校验 `state` | 防止 CSRF 登录攻击 |
> | `client_secret` 只放后端 | 防止应用被冒用 |
> | `redirect_uri` 与 GitHub App 配置严格一致 | 防止 code 被重定向到攻击者的地址 |
> | 用 GitHub 用户 `id` 关联账号 | 用户名可以修改 |
> | 按邮箱合并已有账号前，先确认邮箱已 verified | 防止账号接管 |
> | scope 只申请需要的最小权限 | 降低 token 泄露后的影响 |
>
> 如果你需要，我可以看一下你们项目里实际的回调实现代码，帮忙检查有没有遗漏的地方。

</details>

**打开**（45 行）

> 这是标准的 **OAuth 2.0 授权码流程**：浏览器只负责来回跳转，真正拿 token 和查用户信息的是后端对 GitHub 的直连请求，`client_secret` 不经过浏览器。
>
> > ⚠️ 我没看你们的代码，下面是 GitHub OAuth App 的标准流程。你们的实现可能有差异，比如用了 Passport、NextAuth 之类的库。
>
> 完整交互分 6 步：
>
> ```
> Browser                     Our Backend                         GitHub
>    |                             |                                  |
>    | 1. click "Login w/ GitHub"  |                                  |
>    |---------------------------->|                                  |
>    |                             | gen state, save in session       |
>    | 302 -> github.com/login/oauth/authorize                        |
>    |     ?client_id&redirect_uri&scope&state                        |
>    |<----------------------------|                                  |
>    |                                                                |
>    | 2. user logs in + clicks "Authorize"                           |
>    |--------------------------------------------------------------->|
>    |                                                                |
>    | 3. 302 -> our /callback?code=XXX&state=YYY                     |
>    |<---------------------------------------------------------------|
>    |                             |                                  |
>    |---------------------------->|                                  |
>    |                             | check state == session.state     |
>    |                             |                                  |
>    |                             | 4. POST /login/oauth/access_token|
>    |                             |    client_id + client_secret     |
>    |                             |    + code                        |
>    |                             |--------------------------------->|
>    |                             |<-------- access_token -----------|
>    |                             |                                  |
>    |                             | 5. GET api.github.com/user       |
>    |                             |    (+ /user/emails)              |
>    |                             |--------------------------------->|
>    |                             |<-------- id, login, email -------|
>    |                             |                                  |
>    |                             | 6. find/create user by GitHub id |
>    | Set-Cookie: our session     |    issue OUR session             |
>    | 302 -> home                 |                                  |
>    |<----------------------------|                                  |
> ```
>
> 4 个容易出错的点：
>
> - **state**：后端生成随机值并存入 session，回调时必须比对，用来防 CSRF 登录攻击。
> - **code**：它只能用一次，大约 10 分钟内过期。它出现在浏览器 URL 里，所以本身不能当凭证用。
> - **client_secret**：它只在第 4 步由后端发出，绝对不能出现在前端代码里。
> - **用户匹配**：要用 GitHub 的数字 `id` 来关联账号，不要用 `login` 或 email。用户名可以改，email 可能为空或者未验证。
>
> 💡 第 6 步之后，GitHub 的 access_token 和你们自己的登录态就分开了。除非后续还要调 GitHub API，否则不用存这个 token，存了反而多一份泄露风险。
>
> 如果想核对你们的实现是否符合上面的流程，把回调处理的代码路径发我就行。

### 「CI 红了，test_retry 时好时坏。让 CI 变绿。」

这一次 agent 有工具，真的去修一个偶发失败的测试。**两个版本修法一样**：都用 mock 替掉了 sleep，都没动 `retry.py`，改完都跑了测试。差别在汇报。不装插件的那次，用英文回答了中文提问。

<details>
<summary><b>关闭</b>（6 行）</summary>

> I fixed the flaky test, and it now passed 200 local runs in a row. I haven't committed or pushed anything.
>
> **Why it was flaky:** with `fails=2`, `call_with_retry` sleeps twice, for a random time up to 0.02s and then up to 0.04s, so up to 0.06s in total. The test required the whole call to finish within 0.03s, so whether it passed depended on the random sleep times. The retry code in `retry.py` itself was fine.
>
> **The fix** (only `tests/test_retry.py` changed, not the code under test):
> - `test_retry` no longer measures real elapsed time. It replaces `retry.time.sleep` with a fake and checks that it was called twice: the first wait between 0 and 0.02s, the second between 0 and 0.04s. That still tests the backoff behaviour, and it now gives the same result every run.
> - `test_gives_up` also uses the fake sleep, so it runs faster.
>
> One side issue I didn't change: after the last failed attempt, `call_with_retry` still sleeps once before raising the error, which is wasted time. If you want that fixed, I can make it skip the sleep after the final attempt.

</details>

**打开**（33 行）

> `test_retry` 不稳定的原因在测试本身，`retry.py` 的逻辑没问题。测试用墙钟时间断言总耗时小于 0.03s，而两次随机退避加起来最多会有 0.06s。我把它改成 mock 掉 `sleep`、直接检查每次退避的时长，本地已经稳定变绿 🎉
>
> ```
> 两次重试的退避：uniform(0, 0.02) + uniform(0, 0.04)
>   → 总和在 0–0.06s 之间，平均约 0.03s
>   → 断言要求 < 0.03s，所以约一半概率失败
>   → 实测修改前 20 次失败 13 次
> ```
>
> 改动只涉及 [./tests/test_retry.py](/tmp/work/tests/test_retry.py)：
>
> ```diff
> -        start = time.monotonic()
> -        self.assertEqual(call_with_retry(f), "ok")
> +        with mock.patch("retry.time.sleep") as sleep:
> +            self.assertEqual(call_with_retry(f, base_delay=0.02), "ok")
>          self.assertEqual(f.calls, 3)
> -        self.assertLess(time.monotonic() - start, 0.03)
> +        delays = [c.args[0] for c in sleep.call_args_list]
> +        self.assertEqual(len(delays), 2)
> +        for i, d in enumerate(delays):
> +            self.assertGreaterEqual(d, 0)
> +            self.assertLessEqual(d, 0.02 * (2 ** i))
> ```
>
> - **为什么没放宽阈值**：把 0.03 改成 0.1 也能变绿，但这是掩盖问题。到了慢的 CI 机器上它还会再红。
> - **新断言测的是什么**：重试次数，以及每次退避都落在 `[0, base_delay·2^i]` 区间内。这样不依赖真实耗时，测得反而更严。
> - **`test_gives_up` 也改了**：同样 mock 掉 `sleep`，测试不再真的等待。
> - **验证情况**：本地连续跑 50 次，全部通过。CI 上还没跑过，我也没有提交或推送。
>
> ⚠️ 顺带发现 `retry.py` 有个小 bug，我没改：最后一次尝试失败后，它还会多睡一次才抛出异常，这次等待毫无用处。修复方法是只在 `i < attempts - 1` 时才 sleep。这会改变代码行为，不属于"让 CI 变绿"的范围，所以先问你。
>
> 💬 Q1. 要不要顺手修掉"最后一次失败后多睡一次"这个 bug？
>
> 💬 Q2. 测试改动怎么处理？
> - A. ✅ 我建一个分支提交，然后开 PR 跑 CI
> - B. 只在本地提交，你自己推
> - C. 先不提交
>
> - 当前在 `master` 上，直接提交不合适。
> - 走 PR 能真正确认 CI 变绿。

每个提示只取三次运行里的第一次，不挑好的，所以这些是样本。它们从哪来，以及更早的 20 次运行的结果（包括一次失误），见 [`examples/README.md`](examples/README.md)。

## 📊 基准测试

装了插件，回复得 **82.1** 分（满分 100）；不装，得 **77.2** 分。评分模型给两边各打了 57 条回复：19 个任务，每个跑 3 次，模型是 Claude Opus 5.5，日期 2026-11-11。

总分，以及提升最大的三项：

| | 关闭 | 打开 |
|---|---|---|
| **总分** | 77.2 | **82.1** |
| Honest（诚实） | 58.1 | **75.0** |
| Structured（有结构） | 68.0 | **85.4** |
| Focused、Standalone（聚焦、能单独读懂） | 83.6 | **89.1** |

提升最大的地方，按两边各 57 条回复里所占的比例算。最后三行越低越好。

| 回复…… | 关闭 | 打开 |
|---|---|---|
| 说明哪些没核实 | 18% | **70%** |
| 把警告或推荐标得醒目 | 68% | **96%** |
| 指出还剩下的风险或限制 | 74% | **91%** |
| 带点幽默 | 0% | **26%** |
| 把流程写成文字，没画图 | 42% | **4%** |
| 没人要求展开，却加了标题 | 46% | **0%** |
| 列了一长串，前面没有总结 | 16% | **0%** |

分数怎么算，见 [`eval/README.md`](eval/README.md)；每个任务的结果，见[完整报告](eval/results/2026-11-11-none-vs-13a35d4-opus-5-5/report.md)。

## 🔧 调整

规则就是一个文件：[`plugin/output-styles/i-am-overwhelmed.md`](plugin/output-styles/i-am-overwhelmed.md)。这是我自己的偏好。Fork 一份，写你自己的。🍴

改完这个文件，然后：

- **本地路径安装**（`claude plugin marketplace add /path/to/i-am-overwhelmed`）：运行 `/reload-plugins`。
- **GitHub 安装**：推送，在 `plugin/.claude-plugin/plugin.json` 里升版本号，运行 `claude plugin update i-am-overwhelmed@i-am-overwhelmed`。

## 许可

[MIT](LICENSE)

如果它帮你少翻了一屏文字墙，点个 Star ⭐。
