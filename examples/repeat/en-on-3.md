## ✅ Fixed `test_retry` flakiness

**Cause:** the test failed whenever the random sleeps added up to 0.03s or more. `test_retry` asserted the call finished in under 0.03s. `call_with_retry` sleeps a random amount up to 0.02s, then up to 0.04s. Total sleep can reach 0.06s, so the test failed on some runs.

**Fix (`tests/test_retry.py` only):**
- I mocked `time.sleep`, so the test no longer depends on real time.
- It now checks that the delays are within their allowed bounds: the first in 0–0.02s and the second in 0–0.04s.
- I also mocked sleep in `test_gives_up` so it runs fast.
- `retry.py` is unchanged.

**Verified:** I ran the test 200 times locally and all 200 passed. I haven't seen CI itself run, so I can't confirm it's green there. I also haven't committed anything.

**Weaker check:** the test no longer fails if the backoff gets slow, because it only checks the delay bounds. I think that's the right tradeoff, since a real-time check is what made it flaky.

**Question:** Should I commit this?

- A. Yes, commit it on a new branch (recommended, since you're on `master` and the main branch is `main`)
- B. No, leave it uncommitted
