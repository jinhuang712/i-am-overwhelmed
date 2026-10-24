我已经修好了 `test_retry` 的偶发失败，但这里没有 CI 配置，我没法确认 CI 是否变绿。我在本地用 `PYTHONPATH=. python3 -m unittest tests.test_retry` 跑了一遍，2 个测试都通过。

**原因**：`call_with_retry` 的退避带随机抖动，两次重试最多会睡 0.02 + 0.04 = 0.06 秒。`test_retry` 却断言总耗时小于 0.03 秒，所以抖动抽到较大值时就会失败。

**改动**（只改了 `tests/test_retry.py`）：
- 用 `mock.patch("retry.time.sleep")` 去掉真实等待，测试不再依赖时间。
- 改为断言睡了 2 次，第一次不超过 0.02，第二次不超过 0.04。
- `test_gives_up` 也 mock 了 sleep，跑得更快。

我另外循环了 200 次 `unittest discover`，没有看到失败。不过那条命令的 `grep` 只匹配 "FAIL"，如果 `discover` 因导入错误而报 ERROR，也会被漏掉。所以最可靠的验证是本地那次通过的运行。

`retry.py` 里还有个小问题我没动：最后一次失败后还会多睡一次才抛异常。要不要顺手修，你定。

我没有提交。
