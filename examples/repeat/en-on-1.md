## ✅ Fixed the flaky `test_retry`

I haven't committed anything or run the real CI. Locally, the test passed 200 runs out of 200.

### Cause
- `test_retry` asserted that the retries finish in under 0.03s of real time.
- `call_with_retry` sleeps a random jitter of up to 0.02s after the first failure and up to 0.04s after the second.
- The total can reach 0.06s, so the test failed whenever the random delays added up to more than 0.03s.
- `retry.py` itself is correct. The test was wrong.

### Change (`tests/test_retry.py` only)
- I mocked `time.sleep` in both tests, so they no longer depend on the real clock.
- `test_retry` now checks that there were exactly 2 sleeps and that each is within its allowed bound (≤0.02s and ≤0.04s).
- `test_gives_up` also mocks the sleep, so it runs instantly.

### Things I noticed
- `__pycache__/*.pyc` files are tracked in git. I restored them so they aren't in the diff, but you should probably remove them and add them to `.gitignore`.
- `call_with_retry` also sleeps after the final failed attempt, which wastes time before it raises. I left it alone because it's outside this task.

Do you want me to fix the extra final sleep and untrack the `.pyc` files?
- A. Fix both
- B. Fix only the `.pyc` tracking
- C. Leave both

I recommend B, because it's pure repo hygiene. The final-sleep change alters behavior, so it's worth a separate decision.
