I fixed the flaky `test_retry` by patching `time.sleep` in `tests/test_retry.py`. I haven't pushed or committed anything, so I haven't seen CI go green. The test passed 200 runs in a row locally with no failures, and the file's diff is 11 added and 6 removed lines.

**Cause:** the test timed real sleeps and asserted the whole call took under 0.03s. `retry.py` makes two retries here, sleeping a random amount up to 0.02s and then up to 0.04s. The total can reach 0.06s, so the test failed whenever the jitter came out large. I left `retry.py` unchanged.

**Fix:**
- **`test_retry`:** it now checks the delay values passed to the patched sleep. It asserts there were exactly two delays, the first at most 0.02s and the second at most 0.04s.
- **`test_gives_up`:** it also patches sleep, so it no longer waits on real delays.
- **Runtime:** the tests now finish in about a millisecond.

Run tests with `python3`; plain `python` isn't installed here.
