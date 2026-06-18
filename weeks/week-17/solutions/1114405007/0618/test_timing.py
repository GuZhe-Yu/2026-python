"""Stage 1 — @timeit 裝飾器測試骨架

規格:timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次(預設 3),把每次耗時(float 秒)append 到 f.records
  4. f.last_elapsed = 本次 repeat 的平均耗時
  5. 裝飾器內不准 print
  6. repeat < 1 → raise ValueError(用 raise,不准 assert)

待辦:
  1. 自己打提示詞跟 AI 討論,補齊下面的測試(可再加);規格每條都要有覆蓋
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: stage1 timeit 裝飾器測試"
  4. 寫 timing.py,全綠後 commit: "feat: stage1 實作 timeit 裝飾器"
"""

import unittest
import time

# from timing import timeit  # 完成 timing.py 後解除註解


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        """驗證被裝飾函式的回傳值不變"""
        from timing import timeit

        @timeit()
        def add(a, b):
            return a + b

        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_preserves_function_metadata(self):
        """驗證 functools.wraps 保留了 __name__ 與 __doc__"""
        from timing import timeit

        @timeit()
        def multiply(x, y):
            """兩個數相乘"""
            return x * y

        self.assertEqual(multiply.__name__, "multiply")
        self.assertEqual(multiply.__doc__, "兩個數相乘")

    def test_repeat_records_and_average(self):
        """正常 case: repeat=4, 驗證 records 有 4 筆且 last_elapsed 為平均"""
        from timing import timeit

        @timeit(repeat=4)
        def dummy():
            return 42

        prev_len = len(dummy.records)
        result = dummy()
        self.assertEqual(result, 42)
        self.assertEqual(len(dummy.records), prev_len + 4)
        self.assertIsInstance(dummy.last_elapsed, float)
        self.assertGreater(dummy.last_elapsed, 0)

    def test_default_repeat_is_three(self):
        """驗證預設 repeat=3"""
        from timing import timeit

        @timeit()
        def dummy():
            pass

        prev_len = len(dummy.records)
        dummy()
        self.assertEqual(len(dummy.records), prev_len + 3)

    def test_repeat_below_one_raises_valueerror(self):
        """edge: repeat=0 與 repeat=-1 應拋出 ValueError"""
        from timing import timeit

        for bad in (0, -1):
            with self.assertRaises(ValueError):
                @timeit(repeat=bad)
                def dummy():
                    pass

    def test_repeat_non_integer_raises_typeerror(self):
        """edge: repeat=2.5 或 "abc" 應拋出 TypeError"""
        from timing import timeit

        for bad in (2.5, "abc"):
            with self.assertRaises(TypeError):
                @timeit(repeat=bad)
                def dummy():
                    pass

    def test_exception_in_wrapped_not_recorded(self):
        """edge: 被裝飾函式拋出例外時不計入 records,且例外向上傳遞"""
        from timing import timeit

        @timeit(repeat=3)
        def crash():
            raise RuntimeError("boom")

        prev_records = len(crash.records)
        with self.assertRaises(RuntimeError):
            crash()
        self.assertEqual(len(crash.records), prev_records)


if __name__ == "__main__":
    unittest.main()
