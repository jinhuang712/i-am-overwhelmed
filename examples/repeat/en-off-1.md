I fixed the flaky `test_retry`, and it passed 200 runs in a row locally. I haven't seen CI itself go green, and I haven't committed anything.

**Cause:** the test asserted that real elapsed time was under 0.03s. `call_with_retry` sleeps a random time up to 0.02s after the first failure and up to 0.04s after the second. Two retries can therefore take up to 0.06s, so the test failed whenever the random delays added up past 0.03s.

**Fix:** in `tests/test_retry.py`, `time.sleep` is now mocked in both tests. `test_retry` checks that exactly two sleeps happen, the first at most 0.02s and the second at most 0.04s. `retry.py` is unchanged.

`call_with_retry` also sleeps after the final failed attempt, which is wasted time before it re-raises. I left that alone because it's outside what you asked for.
