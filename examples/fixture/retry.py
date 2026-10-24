import random
import time


def call_with_retry(fn, attempts=3, base_delay=0.02):
    """Call fn(); on failure wait with jitter and try again."""
    last = None
    for i in range(attempts):
        try:
            return fn()
        except ConnectionError as e:
            last = e
            time.sleep(random.uniform(0, base_delay * (2 ** i)))
    raise last
