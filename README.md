<img src="assets/hero.svg" alt="I am overwhelmed. A fed-up user's message to their coding agent, with the reply rules highlighted." width="100%">

# 😵‍💫 i-am-overwhelmed

[English](README.md) · [简体中文](README.zh-CN.md)

**A reply rule that keeps answers easy to read and structured, stays honest, and avoids overwhelming you.**

![license](https://img.shields.io/badge/license-MIT-green) ![version](https://img.shields.io/github/v/tag/jinhuang712/i-am-overwhelmed?label=version) [![benchmark](https://img.shields.io/badge/benchmark-82.1%20vs%2077.2%20without-blue)](#-benchmark)

You are tired, you are doing three other things, and you skim. This plugin makes Claude reply for that reader. Its replies are:

- **Honest**: problems, guesses and unverified claims are said out loud.
- **Simple**: a few lines first, detail when you ask.
- **Structured**: a drawing when the content has a shape, bullets otherwise.
- **Asking**: the facts only you know are asked first, not assumed.
- **Opinionated**: it gives a view, pushes back, and holds it until you convince it.
- **Focused**: one thing at a time, and a note when the talk drifts from the goal.
- **Standalone**: every reply can be read on its own, with no scrolling back.
- **Predictable**: the same formats and the same emoji meanings every time, so you know where to look.

## 🎁 What you get

- **No late surprises**: the reply says now what it did not check and what risk is left.
- **Easier to skim**: a flow is drawn, a long list gets a summary first, and a short answer gets no headings.
- **Asks proactively**: Claude asks you more, to avoid the slop that comes from a guess.
- **A cleaner context**: every reply Claude prints becomes context for the next turn, so structured replies may keep a long session on track.

**The work feels different, too.** The plugin sets only the output style, and its rules are about the reply. Yet with it, the agent feels like this:

- **More honest**: it says what it did not check. Here the benchmark agrees: 70% of replies, against 18%.
- **Checks before it acts**: it investigates before it reasons or changes anything.
- **More curious**: it asks more, and thinks one step further.
- **Pushes back**: it raises objections and offers a better way.
- **Plans instead of dumping**: it splits a task and plans it, instead of pouring out every conclusion at once.
- **Feels quicker**: it overthinks less, gets going sooner, and finds the point earlier.

Why, I can only guess, since I cannot see inside the model: a rule on what a reply must say, such as what was checked, may push the model to do what it takes to say it.

## 📦 Install

**Install for Claude Code**

1. With the CLI:

```bash
claude plugin marketplace add jinhuang712/i-am-overwhelmed
claude plugin install i-am-overwhelmed@i-am-overwhelmed
```

2. With curl:

```bash
curl -fsSL https://raw.githubusercontent.com/jinhuang712/i-am-overwhelmed/master/install-claude.sh | sh
```

**Install with an agent**

Paste this to Claude Code, Codex or another agent:

```text
Install i-am-overwhelmed by following https://raw.githubusercontent.com/jinhuang712/i-am-overwhelmed/master/INSTALL.md
```

Details, caveats and how to remove it: [INSTALL.md](INSTALL.md).

## 🧱 How it works

**The plugin sets one thing: Claude Code's output style.** It adds no hooks, no skills, no tools and no `CLAUDE.md`.

```
Claude Code
├── system prompt
│   ├── coding instructions    kept as they are
│   └── output style           the one thing this plugin sets
├── CLAUDE.md                  untouched
└── hooks, skills, tools       untouched
```

Its rules are about how Claude talks with you, and leave the engineering to Claude Code's own instructions. It is a set of instructions, so expect most replies to follow it, not all.

That is one file per tool. For Claude Code it is [`plugin/output-styles/i-am-overwhelmed.md`](plugin/output-styles/i-am-overwhelmed.md), the plugin's output style, with `force-for-plugin` and `keep-coding-instructions`, so it stays after compaction and keeps Claude Code's own instructions. For Codex it is [`codex/AGENTS.md`](codex/AGENTS.md), the same rules without the Claude Code parts.

Why it is built this way, and why the rules are written the way they are: [PHILOSOPHY.md](PHILOSOPHY.md).

## 👀 See it

Real output, same prompt, plugin off and on. Complete and untrimmed. Each example comes from the benchmark of 2026-11-11, on Claude Opus 5.5 (`claude-opus-5-5`). Click **Off** to open the reply without the plugin. The raw files are in [`examples/`](examples/).

### "SQLite or Postgres for a URL shortener, ~100 users?"

<details>
<summary><b>Off</b> (17 lines)</summary>

> **SQLite.** At ~100 users, it's not close.
>
> **Why SQLite fits:**
> - A URL shortener is mostly reads (redirects), with occasional writes when someone creates a link. SQLite handles that easily, even with thousands of redirects per second.
> - There's no server to run, secure, or back up separately. It's one file, and you can back it up with `sqlite3 db .backup` or Litestream.
> - Lookups by slug are a single indexed primary-key read, which takes microseconds.
>
> **Settings worth turning on:**
> ```sql
> PRAGMA journal_mode = WAL;     -- concurrent reads during writes
> PRAGMA busy_timeout = 5000;    -- avoid "database is locked" errors
> PRAGMA synchronous = NORMAL;   -- safe with WAL, faster
> ```
>
> **When to pick Postgres instead:**
> - You'll run multiple app servers or containers that all need to write to the same DB. SQLite wants a single host.
> - Your platform has ephemeral disks, like Heroku or some serverless setups, and no persistent volume.
> - You expect heavy write-side analytics, such as logging every click with rich metadata at high volume. Even then, batching the inserts usually keeps SQLite fine.
> - Your team already runs Postgres and a managed instance costs you nothing extra to operate.
>
> If you keep your SQL fairly standard, or use an ORM, switching to Postgres later is a small migration.

</details>

**On** (15 lines)

> ✅ **SQLite.** At ~100 users, a URL shortener does one indexed lookup per redirect, and SQLite handles thousands of those per second on one file with nothing to run or patch. (Typical figure, not benchmarked here.)
>
> Postgres only pays off if you run more than one server or host without a persistent disk:
>
> ```
> Where does the app run?
> ├── One server or VM, persistent disk     → SQLite ✅
> ├── Several app instances                 → Postgres
> └── Serverless / ephemeral containers     → Postgres (or hosted SQLite, e.g. Turso)
>     (the file gets wiped on redeploy)
> ```
>
> 3 tips if you pick SQLite:
>
> - **WAL mode**: Turn it on so reads keep working while a write is in progress.
> - **Backups**: Use Litestream, or a nightly copy made with the SQLite backup command. A plain `cp` of a live database file can give you a corrupted copy.
> - **Exit path**: Keep your SQL plain, and moving to Postgres later is about an afternoon of work. 😄
>
> > If "100 users" means 100 accounts but the short links go viral, the read load still stays small. Redirects are cheap.
>
> 💬 Will the app run on a single server with a persistent disk?

### "What happens between the browser, our backend and GitHub after a user clicks 'Sign in with GitHub' on our site?"

<details>
<summary><b>Off</b> (50 lines)</summary>

> I don't see your site's code in this working directory, so this is the standard GitHub OAuth flow (authorization code grant) that almost every "Sign in with GitHub" button uses. If you point me at your auth code, I can map each step to the actual files.
>
> ## The flow, step by step
>
> ```
> Browser                    Your Backend                     GitHub
>    |                            |                              |
> 1  |--- click "Sign in" ------->|                              |
> 2  |<-- 302 to github.com ------|  (sets state cookie)         |
> 3  |------------------------- GET /login/oauth/authorize ----->|
> 4  |<------------------------ login + consent page ------------|
> 5  |------------------------- user approves ------------------>|
> 6  |<-- 302 to your callback ?code=...&state=... --------------|
> 7  |--- GET /callback?code&state ->|                           |
> 8  |                            |--- POST /login/oauth/access_token -->|
> 9  |                            |<-- access_token -------------|
> 10 |                            |--- GET api.github.com/user ->|
> 11 |                            |<-- profile / emails ---------|
> 12 |<-- set session cookie, 302 to app                         |
> ```
>
> ### 1–2. Your backend starts the flow
> The button hits a route like `/auth/github`. The backend:
> - Generates a random **`state`** value and stores it in a short-lived cookie or the server session (CSRF protection).
> - Optionally generates a **PKCE** `code_verifier` and derives a `code_challenge`.
> - Redirects the browser to:
>   ```
>   https://github.com/login/oauth/authorize
>     ?client_id=YOUR_CLIENT_ID
>     &redirect_uri=https://yoursite.com/auth/github/callback
>     &scope=read:user user:email
>     &state=RANDOM
>     [&code_challenge=...&code_challenge_method=S256]
>   ```
>
> ### 3–5. User authenticates at GitHub
> This happens entirely between the browser and GitHub. Your site never sees the user's GitHub password or 2FA. If the user has already authorized your app, GitHub may skip the consent screen.
>
> ### 6. GitHub redirects back
> GitHub sends the browser to your `redirect_uri` with a one-time **`code`** (valid ~10 minutes) and the `state` you sent. The `redirect_uri` must match what's registered in your OAuth App settings.
>
> ### 7. Callback validation
> Your backend checks that `state` matches what it stored. If it doesn't, it rejects the request, because that is a possible CSRF or login-injection attempt.
>
> ### 8–9. Code to token exchange (server to server)
> Your backend POSTs to `https://github.com/login/oauth/access_token` with `client_id`, **`client_secret`**, `code`, `redirect_uri` (and `code_verifier` if you use PKCE). GitHub returns an `access_token`. This is the only step where the client secret is used, which is why it has to happen on the backend.
>
> ### 10–11. Fetch identity
> Your backend calls `GET https://api.github.com/user` (and often `/user/emails`, since the primary email may be private) with `Authorization: Bearer <token>`.
>
> ### 12. Create your own session
> Your backend finds or creates a local user, keyed on GitHub's **numeric user `id`** (not username or email, since those can change). It then issues *your* session cookie or JWT and redirects to the app. From this point, your site uses its own session. The GitHub token is only needed again if you call GitHub APIs on the user's behalf. If you do keep it, store it encrypted.
>
> ## Things worth checking in your implementation
> - The `state` is generated, stored, and verified, not just passed through.
> - The client secret exists only on the server and never in frontend bundles.
> - Users are identified by GitHub `id`. Auto-linking to existing accounts by email should only happen for verified emails.
> - Scopes are minimal. `read:user user:email` is usually enough for login.
> - If it's actually a **GitHub App** instead of an OAuth App, the flow is the same, but tokens expire after 8 hours and come with refresh tokens.
>
> Want me to look at your code and trace where each of these steps happens?

</details>

**On** (32 lines)

> 🤔 I didn't look at your code: the working directory is a temp folder, not your repo. Below is the standard GitHub OAuth web flow, which most "Sign in with GitHub" buttons use. Your site may differ (for example, if it uses Auth0 or NextAuth).
>
> **In short:** the browser bounces to GitHub and back with a one-time `code`. Your backend then trades that code, plus its client secret, for an access token, server to server.
>
> ```
> Browser                    Your backend                     GitHub
>    |                            |                              |
> 1  |-- click "Sign in" -------->|                              |
>    |                            | make random `state`,         |
>    |                            | save it in session/cookie    |
> 2  |<-- 302 redirect -----------|                              |
>    |    github.com/login/oauth/authorize?client_id&            |
>    |    redirect_uri&scope&state                               |
> 3  |---------------------------------------------------------->|
>    |                     user logs in + approves scopes        |
> 4  |<-- 302 to redirect_uri?code=XYZ&state=... ----------------|
> 5  |-- GET /callback?code&state>|                              |
>    |                            | check state == saved state   |
> 6  |                            |-- POST /login/oauth/access_token
>    |                            |   client_id, client_secret, code -->|
>    |                            |<-- access_token -------------|
> 7  |                            |-- GET api.github.com/user -->|
>    |                            |   (+ /user/emails if needed) |
>    |                            |<-- id, login, email ---------|
>    |                            | find or create user by GitHub id
> 8  |<-- Set-Cookie: session ----|                              |
>    |    redirect to app         |                              |
> ```
>
> These 4 points matter most for security:
>
> - **`state`**: a random value that blocks CSRF. A login attacker can't forge the callback without it.
> - **Client secret**: it lives only on the backend. The browser never sees it or the access token.
> - **`code`**: it works once and expires in about 10 minutes.
> - **User identity**: key users by GitHub's numeric `id`, not `login` or email. Users can rename `login`, and emails may be private or unverified.
>
> 💡 If you point me at the repo, I can trace your actual callback handler and check these 4 points against it.

Each prompt shows the first of three runs, not the best, so these are samples. [`examples/README.md`](examples/README.md) says where they come from, and what 20 earlier runs showed, including a miss.

## 📊 Benchmark

With the plugin, replies score **82.1** of 100; without it, **77.2**. A judge model scored 57 replies on each side: 19 tasks, 3 runs each, on Claude Opus 5.5, 2026-11-11.

The overall score, and the three words it gains most on:

| | Off | On |
|---|---|---|
| **Overall** | 77.2 | **82.1** |
| Honest | 58.1 | **75.0** |
| Structured | 68.0 | **85.4** |
| Focused, Standalone | 83.6 | **89.1** |

Where it improves most, as a share of the 57 replies on each side. Lower is better on the last three rows.

| The reply... | Off | On |
|---|---|---|
| says what it did not check | 18% | **70%** |
| makes a warning or a recommendation stand out | 68% | **96%** |
| names a risk or a limit that is left | 74% | **91%** |
| has a light touch of humor | 0% | **26%** |
| writes a flow as text, with no drawing | 42% | **4%** |
| puts headings on an answer, though nobody asked for more detail | 46% | **0%** |
| gives a long list with no summary first | 16% | **0%** |

[`eval/README.md`](eval/README.md) says how the score is made, and [the full report](eval/results/2026-11-11-none-vs-13a35d4-opus-5-5/report.md) has every task.

## 🔧 Tune it

The rules are one file: [`plugin/output-styles/i-am-overwhelmed.md`](plugin/output-styles/i-am-overwhelmed.md). They are my own preferences. Fork it and write yours. 🍴

Edit the file, then:

- **Local-path install** (`claude plugin marketplace add /path/to/i-am-overwhelmed`): run `/reload-plugins`.
- **GitHub install**: push, bump the version in `plugin/.claude-plugin/plugin.json`, run `claude plugin update i-am-overwhelmed@i-am-overwhelmed`.

## License

[MIT](LICENSE)

Star ⭐ if it saved you one scroll through a wall of text.
