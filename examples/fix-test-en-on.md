🎉 `test_retry` is fixed. It passed 30 runs out of 30.

## Cause
- [./retry.py](/private/tmp/claude-501/-Users-jin-huang-dev-projects-i-am-overwhelmed/ad842afa-f550-4cfd-b1a9-dce5446f54db/scratchpad/work-fix-test-en-on.md/retry.py) sleeps a random time between 0 and `0.02 * 2**i` seconds. Two retries can add up to 0.06s.
- The test asserted that the whole call took under 0.03s, so it failed whenever the jitter came out high. The failure was in the test, not in the retry code.

## Fix
I changed only [./tests/test_retry.py](/private/tmp/claude-501/-Users-jin-huang-dev-projects-i-am-overwhelmed/ad842afa-f550-4cfd-b1a9-dce5446f54db/scratchpad/work-fix-test-en-on.md/tests/test_retry.py):
- `time.sleep` is now mocked, so the test no longer depends on real time.
- The timing assertion is replaced by a check that the two sleeps stay within their backoff bounds: `[0, 0.02]` and `[0, 0.04]`.
- `test_gives_up` also mocks the sleep, so it runs instantly.

## Notes
- 💡 I didn't just raise the 0.03s threshold. A looser time limit would still be flaky and would not check the backoff behaviour.
- ⚠️ I couldn't see your CI config. I ran the tests locally with `PYTHONPATH=. python3 -m unittest tests.test_retry`. If CI runs them differently, such as `discover`, the import of `retry` may need a different path.
