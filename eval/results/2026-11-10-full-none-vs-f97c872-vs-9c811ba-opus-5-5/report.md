# Eval 2026-11-10, full run: not valid

This run is kept as a record of what went wrong. It has no scores.

- **No plugin was loaded in the "old" and "new" arms.** `--out` was a relative path, so each `--plugin-dir` was relative too, and every run starts in its own folder. Claude Code skipped the plugin and said nothing. All three arms ran with no plugin. The 32 "old" and "new" runs are deleted.
- **15 runs of the "none" arm are valid** and stay in `raw/`, which is git-ignored. Two more were dropped: the runaway one, and a `shape-zh` reply of one word.
- **`only-you-know-zh` ran away.** As a chat task with no tools, the model wrote made-up tool calls until the output limit: 128,000 tokens and $2.56 in each of three runs, against a $0.15 cap.
- **Every judge call failed** with "You've hit your 5-hour limit". The run used up the account's 5-hour usage limit.
- **Spent**: $17.79 at list prices, of a $25.00 limit. $7.69 of it is the three runaway runs.

The fixes are in `run.py` and `eval.py`: an absolute results path, a check that the plugin loaded, a cap of 16,000 output tokens a reply, and a failed status for a run that hits the usage limit.
