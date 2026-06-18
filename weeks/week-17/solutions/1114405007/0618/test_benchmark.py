"""Stage 3 — benchmark 測試（從零自寫）

驗證 benchmark.py 能正常產出 results.json
"""

import json
import os
import unittest


class TestBenchmark(unittest.TestCase):
    def test_benchmark_runs_and_creates_json(self):
        """執行 benchmark main,確認 results.json 產生"""
        import benchmark
        if os.path.exists("results.json"):
            os.remove("results.json")
        benchmark.main()
        self.assertTrue(os.path.exists("results.json"))

    def test_results_json_has_correct_structure(self):
        """驗證 results.json 包含所有搜尋方法與 n 的數據"""
        import benchmark
        benchmark.main()
        with open("results.json") as f:
            data = json.load(f)
        self.assertIsInstance(data, dict)
        self.assertIn("linear", data)
        self.assertIn("binary", data)
        self.assertIn("set", data)
        self.assertIn("builtin_in", data)
        self.assertIn("builtin_bisect", data)
        for method, records in data.items():
            with self.subTest(method=method):
                for entry in records:
                    self.assertIn("n", entry)
                    self.assertIn("elapsed", entry)

    def test_benchmark_overwrites_old_json(self):
        """edge: 重複執行會覆蓋而非附加"""
        import benchmark
        benchmark.main()
        with open("results.json") as f:
            first = json.load(f)
        benchmark.main()
        with open("results.json") as f:
            second = json.load(f)
        for method in first:
            self.assertEqual(len(first[method]), len(second[method]))

    def test_results_values_are_positive(self):
        """edge: 所有 elapsed 時間應為正數"""
        import benchmark
        benchmark.main()
        with open("results.json") as f:
            data = json.load(f)
        for method, records in data.items():
            for entry in records:
                self.assertGreater(entry["elapsed"], 0)


if __name__ == "__main__":
    unittest.main()
