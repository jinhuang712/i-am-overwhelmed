`test_retry` should no longer flake. It passed 200 runs in a row locally. I haven't pushed anything or checked CI itself, and the changes are uncommitted in `tests/test_retry.py`.

**Cause:** `call_with_retry` sleeps a random jitter after each failure, up to 0.02s after the first and 0.04s after the second. Together that can reach 0.06s, but the test asserted the whole call took under 0.03s. It failed whenever the random delays came out large.

**Fix:** I left `retry.py` alone. The test now mocks `time.sleep` and pins the jitter to its upper bound. It asserts the backoff delays are exactly `[0.02, 0.04]` instead of measuring wall-clock time. I also mocked the sleep in `test_gives_up`, so it no longer sleeps for real.

I ran the tests with `PYTHONPATH=. python3 -m unittest tests.test_retry`, since `tests/` isn't importable as a package. If CI invokes the tests differently, check that its command still finds `retry`.
