# 😵‍💫 i-am-overwhelmed

[English](README.md) · [简体中文](README.zh-CN.md)

**Same answers. Much easier to skim.**
A Claude Code plugin for a tired reader who is doing five other things: a clear verdict first, guesses marked, and one question at the very end.

![license](https://img.shields.io/badge/license-MIT-green) ![version](https://img.shields.io/github/v/tag/jinhuang712/i-am-overwhelmed?label=version)

## 👀 See it

Real output, same prompt, plugin off and on. Trimmed with `…`. [Full text in `examples/`](examples/).

### "SQLite or Postgres for a URL shortener, ~100 users?"

**Off**

> **SQLite.**
>
> For about 100 users, a URL shortener is a read-heavy workload: lots of redirects and few writes. SQLite handles that easily.
>
> - **Performance:** In WAL mode, SQLite serves thousands of reads per second and hundreds of writes per second. That is far more than 100 users will generate.
> - **Operations:** It's a single file, so there's no server to run, patch or secure. …
>
> Settings to use: …
>
> Choose Postgres instead if: …

**On**

> ## Recommendation: SQLite ✅
>
> For ~100 users, SQLite is the better fit.
>
> **Why**
> - A URL shortener is read-heavy (redirects), and SQLite handles that very well.
> - There's no separate server to run, secure, or back up. …
>
> **When I'd pick Postgres instead** …
>
> **Caveat:** I'm assuming a single server. If you plan to run on serverless or several instances, tell me and I'd change this.
>
> **Question:** Where will you deploy it?
> - A. One VPS or container with a persistent disk (SQLite fits, **recommended**)
> - B. Serverless or multiple instances (Postgres fits)
> - C. Not sure yet …

### "CI is red because `test_retry` fails from time to time. Get CI green."

The agent has tools here and fixes a real flaky test. **Both versions fixed it the right way**: mocked the sleep, kept a meaningful assertion, skipped nothing. The difference is the report.

**Off**

> I fixed `test_retry`. It passed 200 runs in a row locally with no failures. I haven't run it in CI itself, and I didn't commit anything.
>
> **Cause:** the test checked that the whole retry took under 0.03s of real time. `call_with_retry` sleeps a random amount up to 0.02s after the first failure and up to 0.04s after the second. …
>
> **Fix:** `retry.py` is unchanged … `time.sleep` is now mocked. …

**On**

> ## `test_retry` flakiness fixed ✅
>
> **Cause:** The test asserted the whole retry finished in under 0.03s. But the retry code sleeps … up to 0.06s. The bug was in the test, not in `retry.py`.
>
> **Fix** (`tests/test_retry.py`, …):
> - The test now mocks `time.sleep`, so it no longer depends on the clock. …
>
> **Verified:** 200 consecutive runs gave 0 failures.
>
> **Caveats:**
> - I didn't change the timing threshold. Raising it would have just made the failure rarer.
> - The repo has no CI config, so I couldn't run CI itself. I only ran the tests locally.

### What actually changes

| | Off | On |
|---|---|---|
| Verdict | In the first line | First line, set apart with a heading and ✅ / 🚫 |
| Structure | Paragraphs and bullets | Headings, short bullets, tables |
| Not sure | Mixed into the text | A named **Caveat** or "I'm guessing" |
| Question | A closing "tell me more" | One question, last, options A / B / C, one recommended |
| Correctness | Good | Good. Not a smarter model, only an easier read. |

## 📦 Install

Paste this to Claude Code:

```text
Install the plugin from github.com/jinhuang712/i-am-overwhelmed:
claude plugin marketplace add jinhuang712/i-am-overwhelmed
claude plugin install i-am-overwhelmed@i-am-overwhelmed
```

Or run those two commands yourself. Restart Claude Code. It turns on by itself.

⚠️ It replaces any output style you picked, such as Explanatory, because Claude Code allows one at a time. To go back, run `claude plugin disable i-am-overwhelmed@i-am-overwhelmed`.

## 📏 The rules

| | |
|---|---|
| 😴 **About me** | Assume I'm tired, multitasking, skimming. |
| 🤝 **Honesty** | Hiding a problem is worse than the problem. Never cheat to pass. Say when guessing. Push back. |
| 💬 **Replies** | Summarize the work. Simple *or* detailed. A title next to every ID. |
| ❓ **Asking** | No question popups. Questions go last, options A / B, with a recommendation. |

That is one file: [`plugin/output-styles/i-am-overwhelmed.md`](plugin/output-styles/i-am-overwhelmed.md). It is the plugin's output style, with `force-for-plugin` and `keep-coding-instructions`, so it stays after compaction and keeps Claude Code's own instructions.

These are my own preferences. Fork it and write yours. 🍴

## 🔧 Tune it

Edit the file above, then:

- **Local-path install** (`claude plugin marketplace add /path/to/i-am-overwhelmed`): run `/reload-plugins`.
- **GitHub install**: push, bump the version in `plugin/.claude-plugin/plugin.json`, run `claude plugin update i-am-overwhelmed@i-am-overwhelmed`.

## License

[MIT](LICENSE)

Star ⭐ if it saved you one scroll through a wall of text.
