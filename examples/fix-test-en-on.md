🎉 `test_retry` is fixed. It passed 200 runs in a row. I can't see your CI, so I haven't confirmed that it's green.

**Cause:** the test required the whole call to finish in under 0.03 s. `retry.py` sleeps for a random time, up to 0.02 s then up to 0.04 s. Whenever the random sleeps added up to more than 0.03 s, the test failed.

**Fix:** in [./tests/test_retry.py](/tmp/work/tests/test_retry.py), `time.sleep` is now mocked. The test checks that each requested delay is within its backoff bound, which is stricter than the old timing check. `test_gives_up` also mocks `sleep`, so it runs instantly.

```diff
-        start = time.monotonic()
-        self.assertLess(time.monotonic() - start, 0.03)
+        with mock.patch("retry.time.sleep") as sleep: ...
+        self.assertTrue(0 <= delays[0] <= 0.02)
+        self.assertTrue(0 <= delays[1] <= 0.04)
```

I only edited the test and left [./retry.py](/tmp/work/retry.py) alone, because the retry code itself works as intended.

Next step: push the change and check CI. This folder isn't a git repo, so I didn't commit.
