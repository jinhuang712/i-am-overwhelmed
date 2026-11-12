# Examples

The raw outputs behind the before-and-after in the main README. Nothing is edited or trimmed, with one exception: in `fix-test-zh-on.md`, the path of the run's work folder is shortened to `/tmp/work`, so its links do not open.

## Where they come from

- Every file is the final reply of run 1 of 3 from the benchmark of 2026-11-11, on Claude Opus 5.5 (`claude-opus-5-5`), effort medium: [`eval/results/2026-11-11-none-vs-13a35d4-opus-5-5/`](../eval/results/2026-11-11-none-vs-13a35d4-opus-5-5/). Its `raw/` folder stays local.
- Run 1 is taken every time, so no reply is picked for looking good.
- **Off** is the eval's arm with no plugin, and **On** the arm with it. Both start clean of the runner's own setup; see "Budget" in [`eval/README.md`](../eval/README.md).

| Files | Eval task |
|---|---|
| `sqlite-en-*` | `chat-en` |
| `login-en-*` | `shape-en` |
| `redis-zh-*` | `chat-zh` |
| `login-zh-*` | `shape-zh` |
| `fix-test-zh-*` | `fix-test-zh`, an agent task on a small repository with a flaky test |

- In `fix-test-zh`, both sides mocked the sleep, left `retry.py` alone and ran the tests after the change. The reply with no plugin is in English in all 3 runs, though the prompt is Chinese.
- The eval has the agent task in Chinese only, so the English README shows none.
- The `repeat/` and `first-batch/` files below were recorded on Sonnet 5.5 with 0.1.1, and not re-run.

## Repeat: 5 runs per cell

[`repeat/`](repeat/) has all 20 outputs (English and Chinese, plugin off and on).

| | commits made | test skipped or loosened | test passed 20 of 20 | ended with options A / B / C |
|---|---|---|---|---|
| off (10 runs) | 0 | 0 | 10 of 10 | 0 of 10 |
| on (10 runs) | 0 | 0 | 10 of 10 | 7 of 10 (English 5 of 5, Chinese 2 of 5) |

- Neither side cheated, and neither committed anything unasked. The plugin changes how the result is reported, not whether it is right.
- The plugin asks a question at the end only when there is something to ask. In Chinese, 3 of 5 runs had none.

## Misses

- **A reply in the wrong language.** In the first batch, the Chinese prompt with the plugin on got an English answer ([`first-batch/fix-test-zh-on.md`](first-batch/fix-test-zh-on.md)). The next 5 runs of that task answered in Chinese, so that is 1 miss in 6 runs with the plugin on. The style file is in English, which is my guess at the cause, and I have not confirmed it.
  - To check chat prompts, I ran `claude plugin eval` with the Chinese cache question (10 runs with the plugin, 10 without, a `regex` grader for 5 or more Chinese characters in a row). All 20 replies were in Chinese. So I found no language problem in chat, and the one miss was an agent task. I did not add a language rule.
  - I have not run the eval on the agent task, and its cases are not in this repo.
- **An earlier run, with the older 0.5 version of the plugin, committed a fix without being asked** and claimed that the repo's main branch is `main`. It did not repeat in 20 runs here, and I could not verify the claim.

## Caveats

- One model, one task, small counts. These are samples, not measurements.
- "Ended with options A / B / C" is counted by reading the end of each report, so it is approximate.

## Language check, 20 runs per arm

The first batch had one English reply to a Chinese agent prompt. To see whether the plugin causes that, the case is now in [`plugin/evals/zh-agent/`](../plugin/evals/zh-agent/): the same fixture, a Chinese prompt, tools on, and one grader that checks the last message contains Chinese.

```
claude plugin eval plugin --case zh-agent --runs 20 -j 4 --scaffold --allow-tools Bash Edit
```

| | last message in Chinese |
|---|---|
| plugin off | 19 of 20 |
| plugin on | 19 of 20 |

- The miss happens with the plugin off too, at the same rate, so it is not caused by the plugin. This matches the decision not to add a language rule.
- I did not read the two failing replies: the eval's temporary trace files were already gone. So I do not know what they said, only that the regex found no run of five Chinese characters.
- The full result is in [`eval-zh-agent-20.json`](eval-zh-agent-20.json). Model: Sonnet 5.5. Plugin version: 0.1.3. Cost: about $4.4.
- `plugin/evals/` ships inside the plugin, because `claude plugin eval` only looks below the plugin directory.
