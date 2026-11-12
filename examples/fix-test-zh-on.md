`test_retry` 不稳定的原因在测试本身，`retry.py` 的逻辑没问题。测试用墙钟时间断言总耗时小于 0.03s，而两次随机退避加起来最多会有 0.06s。我把它改成 mock 掉 `sleep`、直接检查每次退避的时长，本地已经稳定变绿 🎉

```
两次重试的退避：uniform(0, 0.02) + uniform(0, 0.04)
  → 总和在 0–0.06s 之间，平均约 0.03s
  → 断言要求 < 0.03s，所以约一半概率失败
  → 实测修改前 20 次失败 13 次
```

改动只涉及 [./tests/test_retry.py](/tmp/work/tests/test_retry.py)：

```diff
-        start = time.monotonic()
-        self.assertEqual(call_with_retry(f), "ok")
+        with mock.patch("retry.time.sleep") as sleep:
+            self.assertEqual(call_with_retry(f, base_delay=0.02), "ok")
         self.assertEqual(f.calls, 3)
-        self.assertLess(time.monotonic() - start, 0.03)
+        delays = [c.args[0] for c in sleep.call_args_list]
+        self.assertEqual(len(delays), 2)
+        for i, d in enumerate(delays):
+            self.assertGreaterEqual(d, 0)
+            self.assertLessEqual(d, 0.02 * (2 ** i))
```

- **为什么没放宽阈值**：把 0.03 改成 0.1 也能变绿，但这是掩盖问题。到了慢的 CI 机器上它还会再红。
- **新断言测的是什么**：重试次数，以及每次退避都落在 `[0, base_delay·2^i]` 区间内。这样不依赖真实耗时，测得反而更严。
- **`test_gives_up` 也改了**：同样 mock 掉 `sleep`，测试不再真的等待。
- **验证情况**：本地连续跑 50 次，全部通过。CI 上还没跑过，我也没有提交或推送。

⚠️ 顺带发现 `retry.py` 有个小 bug，我没改：最后一次尝试失败后，它还会多睡一次才抛出异常，这次等待毫无用处。修复方法是只在 `i < attempts - 1` 时才 sleep。这会改变代码行为，不属于"让 CI 变绿"的范围，所以先问你。

💬 Q1. 要不要顺手修掉"最后一次失败后多睡一次"这个 bug？

💬 Q2. 测试改动怎么处理？
- A. ✅ 我建一个分支提交，然后开 PR 跑 CI
- B. 只在本地提交，你自己推
- C. 先不提交

- 当前在 `master` 上，直接提交不合适。
- 走 PR 能真正确认 CI 变绿。
