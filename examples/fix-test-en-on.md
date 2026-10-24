## `test_retry` flakiness fixed ✅

**Cause:** The test asserted the whole retry finished in under 0.03s. But the retry code sleeps a random (jittered) delay of up to 0.02s on the first retry and 0.04s on the second. That's up to 0.06s, so the test failed whenever the random delays added up to more than 0.03s. The bug was in the test, not in `retry.py`.

**Fix** (`tests/test_retry.py`, committed as "Make test_retry deterministic by mocking sleep"):
- The test now mocks `time.sleep`, so it no longer depends on the clock.
- Instead of timing the run, it checks the actual behavior: two sleeps happen, the first is at most 0.02s and the second at most 0.04s.
- `test_gives_up` mocks sleep too, so it runs instantly.

**Verified:** 200 consecutive runs gave 0 failures.

**Caveats:**
- I didn't change the timing threshold. Raising it would have just made the failure rarer.
- The repo has no CI config, so I couldn't run CI itself. I only ran the tests locally.
- I committed on `master` without a worktree, since it was a one-file fix.
- Your git status says the main branch is `main`, but the current branch is `master`. Make sure the commit lands on the branch CI watches.
