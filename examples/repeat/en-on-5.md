`test_retry` is fixed. It passed 30 runs in a row, and before the fix it failed about half the time. I didn't run the full CI pipeline and haven't committed anything.

**Cause:** the test was flaky, not the retry code. `call_with_retry` sleeps a random 0–20ms, then 0–40ms, so two retries can take up to 60ms. The test required under 30ms, so it failed whenever the random delays added up past that.

**Fix (in `tests/test_retry.py`):**
- `time.sleep` is mocked, so the tests no longer depend on wall-clock time.
- Instead of the timing check, the test now asserts that there were exactly 2 sleeps, each within its backoff cap (≤20ms and ≤40ms).
- `test_gives_up` also mocks the sleep, so it runs instantly.

I didn't loosen the timing threshold or skip anything. The test still checks the backoff behavior, just not the real elapsed time.

**Not changed:** `retry.py` also sleeps after the final failed attempt, right before it raises. That's wasted time but doesn't make the test fail. It's a one-line fix if you want it.

**Question:** want me to fix that extra sleep in `retry.py`?
- A. Yes, fix it. It's a small change and the code is slightly wrong as is.
- B. No, leave it. That keeps this change limited to getting CI green.

I recommend A.
