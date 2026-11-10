✅ `test_retry` 不再随机失败了:改完后连跑 300 次,0 次失败。

**原因**:[./retry.py](/tmp/work/retry.py) 重试前会随机睡眠,两次重试最多睡 0.06 秒。而测试断言总耗时小于 0.03 秒,所以随机到较长的睡眠时就失败。

**改动**:在 [./tests/test_retry.py](/tmp/work/tests/test_retry.py) 里把 `time.sleep` 换成 mock,不再比较真实耗时,改为检查每次睡眠的时长在退避范围内。`retry.py` 没动。

```diff
-        self.assertLess(time.monotonic() - start, 0.03)
+        delays = [c.args[0] for c in sleep.call_args_list]
+        self.assertEqual(len(delays), 2)
+        self.assertTrue(0 <= delays[0] <= 0.02)
+        self.assertTrue(0 <= delays[1] <= 0.04)
```

⚠️ 这里没有 CI 配置,目录也不是 git 仓库,所以没法验证 CI 本身。我只在本地用 `PYTHONPATH=. python3 -m unittest tests.test_retry` 跑过。

下一步:你把改动提交后看一下 CI 是否变绿。如果 CI 用的是 pytest 或别的启动方式,告诉我命令,我照那个再跑一遍。
