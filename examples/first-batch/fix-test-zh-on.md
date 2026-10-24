## ✅ Fixed `test_retry` flakiness

**Cause:** `test_retry` required the whole call to finish in under 0.03 s. But `retry.py` sleeps a random amount of up to 0.02 s and then up to 0.04 s, so the test failed whenever the jitter came out high.

**Fix:** I changed `tests/test_retry.py` only, and left `retry.py` as it was.
- I mocked `time.sleep` in both tests.
- `test_retry` now checks that there were exactly 2 sleeps, the first in `[0, 0.02]` and the second in `[0, 0.04]`. That tests the backoff itself, and it no longer depends on timing.
- `test_gives_up` also mocks the sleep, so it runs instantly.

**Verified:** I ran the tests 200 times and got 0 failures. I couldn't run CI itself, only the tests locally.

**Not changed:** `call_with_retry` also sleeps after the last failed attempt, right before it raises. That wastes time but doesn't break anything. I can fix it if you want.
