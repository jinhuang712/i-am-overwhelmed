I fixed the flaky test, and it now passed 200 local runs in a row. I haven't committed or pushed anything.

**Why it was flaky:** with `fails=2`, `call_with_retry` sleeps twice, for a random time up to 0.02s and then up to 0.04s, so up to 0.06s in total. The test required the whole call to finish within 0.03s, so whether it passed depended on the random sleep times. The retry code in `retry.py` itself was fine.

**The fix** (only `tests/test_retry.py` changed, not the code under test):
- `test_retry` no longer measures real elapsed time. It replaces `retry.time.sleep` with a fake and checks that it was called twice: the first wait between 0 and 0.02s, the second between 0 and 0.04s. That still tests the backoff behaviour, and it now gives the same result every run.
- `test_gives_up` also uses the fake sleep, so it runs faster.

One side issue I didn't change: after the last failed attempt, `call_with_retry` still sleeps once before raising the error, which is wasted time. If you want that fixed, I can make it skip the sleep after the final attempt.
