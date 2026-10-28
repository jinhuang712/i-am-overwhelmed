🎉 CI 应该绿了：修完后连跑 200 次，全部通过（修之前 20 次里有 10 次失败）。

## 原因
`test_retry` 断言重试总耗时 `< 0.03s`，但 [./retry.py](/private/tmp/claude-501/-Users-jin-huang-dev-projects-i-am-overwhelmed/ad842afa-f550-4cfd-b1a9-dce5446f54db/scratchpad/work-fix-test-zh-on.md/retry.py) 里的 sleep 带随机抖动。两次重试的 sleep 上限合计是 0.02 + 0.04 = 0.06s，所以测试本来就会随机失败。这是测试写错了，代码没问题。

## 改动
只改了 [./tests/test_retry.py](/private/tmp/claude-501/-Users-jin-huang-dev-projects-i-am-overwhelmed/ad842afa-f550-4cfd-b1a9-dce5446f54db/scratchpad/work-fix-test-zh-on.md/tests/test_retry.py)：
- `test_retry`：mock 掉 `time.sleep`，不再断言耗时。改为断言 sleep 恰好调用 2 次，且每次的值落在退避上限内（0~0.02、0~0.04）。
- `test_gives_up`：也 mock 了 sleep，测试不再真的睡觉，变快了。

没有放宽阈值，也没有加重试或 skip。退避逻辑现在是被确定性地检查，而不是碰运气。

## 顺带发现，没改 ⚠️
`call_with_retry` 在最后一次失败之后还会 sleep 一次，然后才抛异常。这次睡眠没有意义，白白增加延迟。这是行为改动，所以我没动。要的话一行就能修。

另外，这个目录不是 git 仓库，我没法看 CI 配置，也没法确认 CI 的 Python 版本和本地一致。
