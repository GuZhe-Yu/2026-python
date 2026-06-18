import functools
import time


def timeit(repeat=3):
    if not isinstance(repeat, int):
        raise TypeError("repeat must be an integer")
    if repeat < 1:
        raise ValueError("repeat must be >= 1")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            times = []
            for _ in range(repeat):
                start = time.perf_counter()
                try:
                    result = func(*args, **kwargs)
                except Exception:
                    raise
                elapsed = time.perf_counter() - start
                times.append(elapsed)
            wrapper.records.extend(times)
            wrapper.last_elapsed = sum(times) / repeat
            return result
        wrapper.records = []
        return wrapper
    return decorator
