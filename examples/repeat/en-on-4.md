Fixed `test_retry` locally, but I haven't pushed it or seen CI run. It passed 300 runs in a row with no failures.

## Cause
- `test_retry` asserted that real elapsed time was under 0.03s.
- `call_with_retry` sleeps a random 0 to 0.02s after the first failure, then 0 to 0.04s after the second. That adds up to as much as 0.06s, so the test failed whenever the random sleeps came out long.

## Fix
- **Change:** in `tests/test_retry.py`, `time.sleep` is now mocked. The test checks that there were 2 sleeps and that each was within its allowed range (at most 0.02s and 0.04s). `test_gives_up` mocks the sleep too, so it no longer waits.
- **Not touched:** `retry.py`.

## Things to know
- 🧹 `__pycache__/*.pyc` files are tracked in git and show as modified. I didn't commit anything. They probably shouldn't be tracked, so you may want to `.gitignore` them.
- 🐛 `retry.py` also sleeps after the final failed attempt, just before it raises. That's wasted time, not a cause of this failure, so I left it alone.

Do you want me to fix the extra sleep and untrack the `.pyc` files?
- A. Yes, do both.
- B. Only untrack the `.pyc` files.
- C. No, leave it as is.

I'd pick A. Both are small, and the extra sleep slows every failed call.
