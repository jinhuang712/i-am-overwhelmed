`test_retry` now passes 50 runs in a row. I haven't run CI itself, and I haven't committed anything.

**Cause:** the test asserted that the whole retry took under 0.03s. `call_with_retry` sleeps a random time up to 0.02s after the first failure and up to 0.04s after the second. The total could reach 0.06s, so the test failed whenever the jitter came out high.

**Fix:** in `tests/test_retry.py` I patched `retry.time.sleep` and replaced the timing assertion with checks on the delays. The test now asserts two sleeps, the first at most 0.02s and the second at most 0.04s. I also patched `sleep` in `test_gives_up`, so that test no longer waits in real time.

`call_with_retry` also sleeps after the last failed attempt, right before it re-raises. That wait is pointless. I left it alone because it changes behavior outside the test, but it's a one-line change if you want it.
