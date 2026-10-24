`test_retry` should no longer flake. It passed 30 runs in a row locally. I haven't run CI itself or committed anything.

**Cause:** the test asserted the retry finishes in under 0.03s. `call_with_retry` sleeps a random amount of up to 0.02s, then up to 0.04s, so the real total can reach 0.06s. The test failed whenever the random delays came out high.

**Fix (in `tests/test_retry.py` only):** the tests now mock `time.sleep`. `test_retry` checks that two sleeps happen and that each stays within its backoff bound (0.02s and 0.04s). `test_gives_up` also mocks the sleep, so it no longer waits on real delays. `retry.py` is unchanged.

**Not fixed:** `call_with_retry` also sleeps after the final failed attempt, just before it re-raises. That wastes time but doesn't break any test.
