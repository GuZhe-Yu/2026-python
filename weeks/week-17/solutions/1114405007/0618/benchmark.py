"""benchmark — 使用 @timeit 比較五種搜尋方式效能"""

import json
import random
import bisect

from search import linear_search, binary_search, set_search
from timing import timeit


@timeit(repeat=5)
def timed_linear(data, target):
    return linear_search(data, target)


@timeit(repeat=5)
def timed_binary(data, target):
    return binary_search(data, target)


@timeit(repeat=5)
def timed_set(data, target):
    return set_search(data, target)


@timeit(repeat=5)
def timed_in(data, target):
    return target in data


@timeit(repeat=5)
def timed_bisect(data, target):
    idx = bisect.bisect_left(data, target)
    return idx < len(data) and data[idx] == target


def main():
    ns = [100, 500, 1000, 5000, 10000, 50000]
    results = {
        "linear": [],
        "binary": [],
        "set": [],
        "builtin_in": [],
        "builtin_bisect": [],
    }
    for n in ns:
        data = [random.randint(0, 100000) for _ in range(n)]
        sorted_data = sorted(data)
        target = random.choice(data)

        timed_linear(data, target)
        results["linear"].append({"n": n, "elapsed": timed_linear.last_elapsed})

        timed_binary(sorted_data, target)
        results["binary"].append({"n": n, "elapsed": timed_binary.last_elapsed})

        timed_set(data, target)
        results["set"].append({"n": n, "elapsed": timed_set.last_elapsed})

        timed_in(data, target)
        results["builtin_in"].append({"n": n, "elapsed": timed_in.last_elapsed})

        timed_bisect(sorted_data, target)
        results["builtin_bisect"].append({"n": n, "elapsed": timed_bisect.last_elapsed})

    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()
