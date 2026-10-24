import time
import unittest

from retry import call_with_retry


class Flaky:
    def __init__(self, fails):
        self.fails = fails
        self.calls = 0

    def __call__(self):
        self.calls += 1
        if self.calls <= self.fails:
            raise ConnectionError("boom")
        return "ok"


class TestRetry(unittest.TestCase):
    def test_retry(self):
        f = Flaky(fails=2)
        start = time.monotonic()
        self.assertEqual(call_with_retry(f), "ok")
        self.assertEqual(f.calls, 3)
        self.assertLess(time.monotonic() - start, 0.03)

    def test_gives_up(self):
        with self.assertRaises(ConnectionError):
            call_with_retry(Flaky(fails=5))


if __name__ == "__main__":
    unittest.main()
