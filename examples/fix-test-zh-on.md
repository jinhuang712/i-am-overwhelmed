## ✅ 已修复 `test_retry` 的随机失败

**原因**
- `test_retry` 断言真实耗时 `< 0.03s`。
- 但 `retry.py` 的抖动退避最多会睡 `0.02 + 0.04 = 0.06s`。
- 所以每次随机到较长的睡眠时间,测试就失败。这是测试写错了,不是 `retry.py` 的 bug。

**改动**(只改了 `tests/test_retry.py`)
- 用 `mock` 替换 `time.sleep`,测试不再依赖真实时间。
- 改为断言每次睡眠都在预期范围内:第 1 次在 `[0, 0.02]`,第 2 次在 `[0, 0.04]`。
- `test_gives_up` 也 mock 了 `sleep`,不再白睡。

**验证**
- 连续跑 200 次,全部 `OK`。

**没做的**
- 没有 commit。
- 仓库里没有 CI 配置文件(没找到 `.github/workflows`),所以我没法在 CI 上直接确认,只在本地验证过。

**一个提示**
- `__pycache__/*.pyc` 被提交进了仓库,建议加 `.gitignore` 并移除。我没动。

要我现在 commit 并清理 `.pyc` 吗?

- A. 只 commit 测试修复(推荐,改动最小,先让 CI 变绿)
- B. 连 `.pyc` 清理和 `.gitignore` 一起做,分成两个 commit
- C. 先不 commit
