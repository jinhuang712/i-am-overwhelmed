# 😵‍💫 i-am-overwhelmed

[English](README.md) · [简体中文](README.zh-CN.md)

**A reply rule that keeps answers easy to read and structured, stays honest, and avoids overwhelming you.**

![license](https://img.shields.io/badge/license-MIT-green) ![version](https://img.shields.io/github/v/tag/jinhuang712/i-am-overwhelmed?label=version)

## 📦 Install

Paste this to Claude Code:

```text
Install the plugin from github.com/jinhuang712/i-am-overwhelmed:
claude plugin marketplace add jinhuang712/i-am-overwhelmed
claude plugin install i-am-overwhelmed@i-am-overwhelmed
```

Or paste this to Codex:

```text
Append the contents of https://raw.githubusercontent.com/jinhuang712/i-am-overwhelmed/master/codex/AGENTS.md to ~/.codex/AGENTS.md, then tell me to start a new session.
```

Details, caveats and how to remove it: [INSTALL.md](INSTALL.md).

## 👀 See it

Real output, same prompt, plugin off and on. Complete and untrimmed. Every example ran on Sonnet 5.5 (`claude-sonnet-5-5`); the plugin-on ones used plugin 0.1.7. The raw files are in [`examples/`](examples/).

### "SQLite or Postgres for a URL shortener, ~100 users?"

**Off**

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

**On**

> # ✅ SQLite
>
> At ~100 users, a URL shortener is a read-heavy workload with tiny rows. SQLite handles that easily.
>
> ## Why SQLite
> - **Zero ops:** no server, no credentials, no connection pool. Backup is copying one file (or Litestream).
> - **Fast reads:** redirects are simple key lookups, in-process with no network hop.
> - **Enough write capacity:** with `PRAGMA journal_mode=WAL`, it handles thousands of writes per second. Click counters at 100 users won't come close.
>
> ## When I'd pick Postgres instead
> - ⚠️ You need **multiple app servers** writing to the same DB.
> - ⚠️ Your host has an **ephemeral disk** (some PaaS, serverless), so a local file won't survive.
> - You expect to grow **100x** soon, or want managed backups and replicas.
>
> ## 💡 Tip
> Keep your queries standard and use an ORM or query builder. Moving to Postgres later is then a config change plus a data copy, not a rewrite.
>
> 🤔 Postgres for 100 users is over-engineering, unless you already run it and it costs you nothing extra.
>
> Where will this be deployed (single VPS, container with a volume, or serverless)? That's the one thing that could change my answer.
> - A. Single VPS or container with a persistent volume → SQLite (recommended)
> - B. Serverless or ephemeral disk → Postgres

### "CI is red because `test_retry` fails from time to time. Get CI green."

Here the agent has tools and fixes a real flaky test. **Both versions fixed it the right way**: mocked the sleep, kept a meaningful assertion, skipped nothing. The difference is the report.

**Off**

> I fixed the flaky `test_retry`, and it passed 200 runs in a row locally. I haven't seen CI itself go green, and I haven't committed anything.
>
> **Cause:** the test asserted that real elapsed time was under 0.03s. `call_with_retry` sleeps a random time up to 0.02s after the first failure and up to 0.04s after the second. Two retries can therefore take up to 0.06s, so the test failed whenever the random delays added up past 0.03s.
>
> **Fix:** in `tests/test_retry.py`, `time.sleep` is now mocked in both tests. `test_retry` checks that exactly two sleeps happen, the first at most 0.02s and the second at most 0.04s. `retry.py` is unchanged.
>
> `call_with_retry` also sleeps after the final failed attempt, which is wasted time before it re-raises. I left that alone because it's outside what you asked for.

**On**

> 🎉 `test_retry` is fixed. It passed 30 runs out of 30.
>
> ## Cause
> - [./retry.py](/private/tmp/claude-501/-Users-jin-huang-dev-projects-i-am-overwhelmed/ad842afa-f550-4cfd-b1a9-dce5446f54db/scratchpad/work-fix-test-en-on.md/retry.py) sleeps a random time between 0 and `0.02 * 2**i` seconds. Two retries can add up to 0.06s.
> - The test asserted that the whole call took under 0.03s, so it failed whenever the jitter came out high. The failure was in the test, not in the retry code.
>
> ## Fix
> I changed only [./tests/test_retry.py](/private/tmp/claude-501/-Users-jin-huang-dev-projects-i-am-overwhelmed/ad842afa-f550-4cfd-b1a9-dce5446f54db/scratchpad/work-fix-test-en-on.md/tests/test_retry.py):
> - `time.sleep` is now mocked, so the test no longer depends on real time.
> - The timing assertion is replaced by a check that the two sleeps stay within their backoff bounds: `[0, 0.02]` and `[0, 0.04]`.
> - `test_gives_up` also mocks the sleep, so it runs instantly.
>
> ## Notes
> - 💡 I didn't just raise the 0.03s threshold. A looser time limit would still be flaky and would not check the backoff behaviour.
> - ⚠️ I couldn't see your CI config. I ran the tests locally with `PYTHONPATH=. python3 -m unittest tests.test_retry`. If CI runs them differently, such as `discover`, the import of `retry` may need a different path.

### What actually changes

| | Off | On |
|---|---|---|
| Verdict | In the first line | First line, set apart with a heading and ✅ or 🎉 |
| Structure | Paragraphs and bullets | Headings, short bullets, tables |
| Not sure | Mixed into the text | Named and marked: ⚠️ warning, 🤔 doubt, 💡 tip |
| Attitude | Only in the words | Also in the emoji, such as 🤔 for doubt |
| Question | Usually none | When there is one: last, options A / B / C, one recommended |
| Correctness | Good | Good. Not a smarter model, only an easier read. |

One run per prompt, so these are samples. [`examples/README.md`](examples/README.md) says what 20 more runs showed, including a miss.

## 📏 The rules

| | |
|---|---|
| 😴 **About me** | Assume I'm tired, multitasking, skimming, and want your opinion. |
| 🤝 **Honesty** | Hiding a problem is worse than the problem. Never cheat to pass. Say when guessing. Push back. |
| 💬 **Replies** | Summarize the work. Simple *or* detailed. A title next to every ID. |
| 🎨 **Formatting** | Headings, tables, code blocks. Emoji with fixed meanings. Files as links, spaced URLs, quoted code instead of line numbers, `diff` blocks. |
| ❓ **Asking** | No question popups. Questions go last, options A / B, with a recommendation. |

That is one file per tool. For Claude Code it is [`plugin/output-styles/i-am-overwhelmed.md`](plugin/output-styles/i-am-overwhelmed.md), the plugin's output style, with `force-for-plugin` and `keep-coding-instructions`, so it stays after compaction and keeps Claude Code's own instructions. For Codex it is [`codex/AGENTS.md`](codex/AGENTS.md), the same rules without the Claude Code parts.

These are my own preferences. Fork it and write yours. 🍴

## 🔧 Tune it

Edit the file above, then:

- **Local-path install** (`claude plugin marketplace add /path/to/i-am-overwhelmed`): run `/reload-plugins`.
- **GitHub install**: push, bump the version in `plugin/.claude-plugin/plugin.json`, run `claude plugin update i-am-overwhelmed@i-am-overwhelmed`.

## 📚 References

Background reading for the rules above. It is not proof: none of these studies tested chat replies, so each rule is carried over by inference from web pages, lab tasks and clinical handoffs.

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

## License

[MIT](LICENSE)

Star ⭐ if it saved you one scroll through a wall of text.
