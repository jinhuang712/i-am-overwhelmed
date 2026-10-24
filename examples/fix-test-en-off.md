I fixed `test_retry`. It passed 200 runs in a row locally with no failures. I haven't run it in CI itself, and I didn't commit anything.

**Cause:** the test checked that the whole retry took under 0.03s of real time. `call_with_retry` sleeps a random amount up to 0.02s after the first failure and up to 0.04s after the second. The two sleeps can add up to 0.06s, so the test failed whenever the random delays came out long.

**Fix:** `retry.py` is unchanged, since the retry code itself is fine. In `tests/test_retry.py`, `time.sleep` is now mocked. The test checks that exactly two sleeps happened and that each stayed within its backoff cap (0.02s and 0.04s). `test_gives_up` also mocks the sleep, so it no longer waits on real delays.
