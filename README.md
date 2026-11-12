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

- **A cleaner context, and less drift**: every reply Claude prints becomes context for the next turn, so short, structured replies keep a long session on track.
- **Fewer wrong turns**: Claude asks before it assumes, so the work is not built on a guess about you.
- **Less to read**: the answer comes first, and the detail waits until you ask for it.
- **No late surprises**: what is broken, guessed or unverified is said now, not found later.

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

It changes how Claude talks with you, and leaves how Claude does the work alone. It is a set of instructions, so expect most replies to follow it, not all.

That is one file per tool. For Claude Code it is [`plugin/output-styles/i-am-overwhelmed.md`](plugin/output-styles/i-am-overwhelmed.md), the plugin's output style, with `force-for-plugin` and `keep-coding-instructions`, so it stays after compaction and keeps Claude Code's own instructions. For Codex it is [`codex/AGENTS.md`](codex/AGENTS.md), the same rules without the Claude Code parts.

Why it is built this way, and why the rules are written the way they are: [PHILOSOPHY.md](PHILOSOPHY.md).

## 👀 See it

Real output, same prompt, plugin off and on. Complete and untrimmed. Every example ran on Sonnet 5.5 (`claude-sonnet-5-5`); the plugin-on ones were recorded on 2026-11-10 with the rules in this repo. Click **Off** to open the reply without the plugin. The raw files are in [`examples/`](examples/).

### "SQLite or Postgres for a URL shortener, ~100 users?"

<details>
<summary><b>Off</b> (17 lines)</summary>

> **SQLite.**
>
> For about 100 users, a URL shortener is a read-heavy workload with tiny rows. SQLite handles that easily.
>
> - **Simplicity:** There's no server to run, secure, or back up separately. The database is one file.
> - **Performance:** Redirect lookups by primary key on a short code take microseconds. With WAL mode on, SQLite handles thousands of reads per second and enough writes for 100 users.
> - **Cost:** It needs no extra process or memory, so a small VPS is plenty.
>
> **Setup tips**
> - Enable WAL: `PRAGMA journal_mode=WAL;`
> - Set `PRAGMA busy_timeout=5000;` and `PRAGMA synchronous=NORMAL;`
> - Make the short code the primary key or put a unique index on it.
> - Record click counts in a separate table, or batch the updates. That keeps write contention off the redirect path.
> - Back it up with `sqlite3 db ".backup file"` or Litestream, and don't copy the live file.
>
> **When to pick Postgres**
> - You expect to run multiple app servers writing to the same database.
> - You expect heavy concurrent writes, such as high-volume click analytics.
> - Your platform has no persistent disk, as with some serverless setups.
> - You want Postgres-specific features or a managed database with built-in backups.
>
> If you outgrow SQLite, migrating a table this simple is easy. Start with SQLite.

</details>

**On** (15 lines)

> ✅ **SQLite.** At ~100 users, a shortener is read-heavy and tiny, so SQLite handles it with zero ops.
>
> ```
> Request ──► App ──► SQLite file
>                     (one file, backup = copy)
> ```
>
> - **Why**: no separate server to run, patch, or pay for
> - **Speed**: redirects are simple key lookups, so microseconds
> - **Setup**: turn on WAL mode (write-ahead log, lets reads and writes overlap) with `PRAGMA journal_mode=WAL;`
> - **Backups**: use Litestream or a nightly copy
>
> ⚠️ **Premise to check**: SQLite assumes one app server with a local disk. If you deploy on serverless or run several instances, Postgres fits better.
>
> 🤔 **Switch to Postgres if**:
> - You need multiple app servers
> - Click analytics produce heavy concurrent writes
> - You plan to grow well beyond 100 users
>
> Q1. Will this run on a single server with a persistent disk?

### "After a user clicks 'Sign in with GitHub' on our site, how do the browser, our backend and GitHub talk to each other, step by step?"

<details>
<summary><b>Off</b> (62 lines)</summary>

> Here is the standard OAuth 2.0 authorization code flow that "Sign in with GitHub" uses. I haven't looked at your code, so check the details (endpoints, scopes, session handling) against your implementation.
>
> ## Step by step
>
> **1. Browser → your backend: start login**
> The user clicks the button, which goes to something like `GET /auth/github`.
>
> **2. Backend → browser: redirect to GitHub**
> Your backend generates a random `state` value, stores it (in the session or a signed cookie), and replies with a `302` to:
> ```
> https://github.com/login/oauth/authorize
>   ?client_id=<your client id>
>   &redirect_uri=https://yoursite.com/auth/github/callback
>   &scope=read:user user:email
>   &state=<random>
> ```
> Optionally, it also sends a PKCE `code_challenge`.
>
> **3. Browser ↔ GitHub: login and consent**
> The browser follows the redirect. The user logs in to GitHub if needed and approves the requested scopes. Your backend is not involved here, and your site never sees the user's GitHub password.
>
> **4. GitHub → browser → your backend: callback**
> GitHub redirects the browser to your `redirect_uri`:
> ```
> GET /auth/github/callback?code=<short-lived code>&state=<same state>
> ```
> The `code` is single-use and expires quickly, and it is not an access token.
>
> **5. Backend: verify `state`**
> Your backend compares the `state` in the URL with the one it stored. If they don't match, it rejects the request. This protects against login CSRF.
>
> **6. Backend → GitHub: exchange the code for a token** (server to server)
> ```
> POST https://github.com/login/oauth/access_token
>   client_id, client_secret, code, redirect_uri  (+ code_verifier if PKCE)
> ```
> GitHub responds with an `access_token`. The `client_secret` is sent only here, from your server, never through the browser.
>
> **7. Backend → GitHub API: fetch the user's identity**
> ```
> GET https://api.github.com/user
> Authorization: Bearer <access_token>
> ```
> If you need the email, also call `GET /user/emails`. Use the numeric `id` as the stable identifier, since usernames and emails can change.
>
> **8. Backend: create or link the local account**
> Look up the user by GitHub `id`, creating a record if none exists. Then create your own session.
>
> **9. Backend → browser: log the user in**
> Your backend sets a session cookie (`HttpOnly`, `Secure`, `SameSite=Lax`) and redirects to your app, for example `302 /dashboard`. From then on the browser authenticates to your backend with that cookie. GitHub is no longer involved unless you store the access token to call its API later.
>
> ## Diagram
>
> ```
> Browser            Your backend              GitHub
>   | --click------->  |                         |
>   | <--302 + state-- |                         |
>   | ------------------authorize?client_id...-->|
>   | <-----------------login/consent------------>|
>   | <-----------------302 ?code&state----------|
>   | --callback?code&state-->|                  |
>   |                  | --POST access_token---->|
>   |                  | <--access_token---------|
>   |                  | --GET /user------------>|
>   |                  | <--profile--------------|
>   | <--Set-Cookie, 302 /app--|                 |
> ```
>
> ## Common pitfalls
> - Skipping the `state` check.
> - Treating the email or username as the identity key instead of the GitHub `id`.
> - Exposing `client_secret` to frontend code.
> - Using a `redirect_uri` that doesn't exactly match the one registered in the GitHub OAuth app.
> - Storing the access token unencrypted if you keep it.
>
> If you'd like, I can point to where each step lives in your codebase. I'd need you to open or point me at the project, since the current directory doesn't contain it.

</details>

**On** (24 lines)

> Here is the standard OAuth 2.0 "authorization code" flow. I'm guessing your site uses it and haven't checked your code.
>
> ```
> Browser              Backend                GitHub
>    |                    |                      |
> 1  |--- click --------->|                      |
> 2  |<-- 302 to GitHub --|                      |
>    |    (client_id, scope, state)              |
> 3  |------------ login + consent ------------->|
> 4  |<----------- 302 to /callback -------------|
>    |             (code, state)                 |
> 5  |--- /callback ----->|                      |
>    |    (code, state)   |                      |
> 6  |                    |--- code + secret --->|
> 7  |                    |<-- access_token -----|
> 8  |                    |--- GET /user ------->|
> 9  |                    |<-- profile ----------|
> 10 |<-- session cookie -|                      |
> ```
>
> - **Steps 1-4**: the browser is only a messenger. It carries redirects between your backend and GitHub.
> - **Step 6**: the one that matters. The `code` is short-lived and useless alone. Your backend swaps it for a token using `client_secret`, which never reaches the browser ✅
> - **Step 5**: the backend must check that `state` matches what it issued in step 2. Skipping this opens a CSRF hole (forged login) ⚠️
> - **Step 10**: your backend creates its own session. GitHub's token usually stays server-side.
>
> 💡 If your app is a SPA or mobile app with no secret, use PKCE (a one-time proof sent with the code) instead.
>
> Want me to check your code against these steps, especially the `state` check? Answer yes or no.

### "CI is red because `test_retry` fails from time to time. Get CI green."

Here the agent has tools and fixes a real flaky test. **Both versions fixed it the right way**: mocked the sleep, kept a meaningful assertion, skipped nothing. The difference is the report.

<details>
<summary><b>Off</b> (4 lines)</summary>

> I fixed the flaky `test_retry`, and it passed 200 runs in a row locally. I haven't seen CI itself go green, and I haven't committed anything.
>
> **Cause:** the test asserted that real elapsed time was under 0.03s. `call_with_retry` sleeps a random time up to 0.02s after the first failure and up to 0.04s after the second. Two retries can therefore take up to 0.06s, so the test failed whenever the random delays added up past 0.03s.
>
> **Fix:** in `tests/test_retry.py`, `time.sleep` is now mocked in both tests. `test_retry` checks that exactly two sleeps happen, the first at most 0.02s and the second at most 0.04s. `retry.py` is unchanged.
>
> `call_with_retry` also sleeps after the final failed attempt, which is wasted time before it re-raises. I left that alone because it's outside what you asked for.

</details>

**On** (16 lines)

> 🎉 `test_retry` is fixed. It passed 30 runs out of 30, where before it failed in 5 of 6. I only ran the tests locally, since I can't see your CI.
>
> The test asserted that the whole call finishes in under 0.03s of real time. The retry code sleeps a random 0–0.02s, then 0–0.04s, which averages about 0.03s. So the test failed most runs by design.
>
> I left [./retry.py](/tmp/work/retry.py) alone because its backoff is correct.
>
> The fix is in [./tests/test_retry.py](/tmp/work/tests/test_retry.py). It no longer waits on the clock:
>
> ```diff
> -        start = time.monotonic()
> -        self.assertEqual(call_with_retry(f), "ok")
> -        self.assertLess(time.monotonic() - start, 0.03)
> +        with mock.patch("retry.time.sleep") as sleep:
> +            self.assertEqual(call_with_retry(f), "ok")
> +        # delay i must be within [0, base_delay * 2**i]
> ```
>
> - **Patched sleep**: `time.sleep` is mocked, so the tests also run faster.
> - **Bounds check**: the test now checks that the two delays stay within their backoff limits. That's a stronger check than the old time limit.
> - **Other test**: I patched sleep in `test_gives_up` too.
>
> Next step: push it and confirm CI goes green.

One run per prompt, so these are samples. [`examples/README.md`](examples/README.md) says how they were made, and what 20 earlier runs showed, including a miss.

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
