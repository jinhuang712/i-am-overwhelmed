I fixed `test_retry` and it passed 30 runs in a row locally. I haven't pushed it or seen CI run, and I haven't committed the change.

**Cause:** the test asserted the whole retry took under 0.03s of real time. `call_with_retry` sleeps a random amount up to 0.02s after the first failure and up to 0.04s after the second. Those two sleeps can add up to 0.06s, so the test failed whenever the random delays were long.

**Fix:** in `tests/test_retry.py`, `test_retry` now patches `time.sleep`. It checks that there were exactly two sleeps, that the first was at most 0.02s and the second at most 0.04s. I also patched `sleep` in `test_gives_up` so it doesn't wait on real delays. `retry.py` is unchanged.
