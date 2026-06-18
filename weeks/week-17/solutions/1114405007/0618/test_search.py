"""Stage 2 — 搜尋正確性測試骨架

規格:search.py 的 linear_search / binary_search / set_search 必須
  1. 一律不可修改傳入的 data(測試要驗)
  2. 回傳型別「不一致」,共用測試時要小心:
        - linear_search(data, target) -> int   找到回 index,找不到回 -1
        - binary_search(data, target) -> int   找到回 index,找不到回 -1
        - set_search(data, target)    -> bool  回傳是否存在
  3. binary_search 的前提是 data 已排序;收到未排序 data 的行為,
      自己定義並在 docstring 寫清楚,測試也要對得上你的定義

設計要求:三個函式共用同一組測試——用迴圈 + subTest,不要複製貼上三份。
  因為回傳型別不同,subTest 裡要把「找到/找不到」轉成可比較的共同判準
  (例:linear/binary 看 index 是否 >= 0,set 看 bool)——怎麼轉自己想。

待辦:
  1. 自己打提示詞跟 AI 討論,補齊測試——一般案例、edge case(空 list?重複值?
     目標不存在?)、「不可修改傳入 data」都要覆蓋;AI 給的齊不齊,自己驗收
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: stage2 搜尋正確性測試"
  4. 寫 search.py,全綠後 commit: "feat: stage2 實作三種搜尋"
"""

import copy
import unittest

from search import linear_search, binary_search, set_search

SEARCH_FUNCTIONS = [linear_search, binary_search, set_search]


def _found(result, func):
    """統一判準: linear/binary 回 index >= 0 算找到,set 回 True 算找到"""
    if func in (linear_search, binary_search):
        return result >= 0
    return result


class TestSearchFunctions(unittest.TestCase):
    def test_found_target_returns_positive(self):
        """一般案例:存在目標,所有搜尋應回傳「找到」"""
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        sorted_data = sorted(data)
        target = 5
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                if func.__name__ == "binary_search":
                    result = func(sorted_data, target)
                else:
                    result = func(data, target)
                self.assertTrue(_found(result, func))

    def test_not_found_returns_negative(self):
        """一般案例:不存在目標,所有搜尋應回傳「沒找到」"""
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        sorted_data = sorted(data)
        target = 99
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                if func.__name__ == "binary_search":
                    result = func(sorted_data, target)
                else:
                    result = func(data, target)
                self.assertFalse(_found(result, func))

    def test_input_not_mutated(self):
        """驗證搜尋後 data 內容不變"""
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        original = copy.deepcopy(data)
        sorted_data = sorted(data)
        sorted_original = copy.deepcopy(sorted_data)
        target = 5
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                if func.__name__ == "binary_search":
                    func(sorted_data, target)
                    self.assertEqual(sorted_data, sorted_original)
                else:
                    func(data, target)
                    self.assertEqual(data, original)

    def test_empty_list(self):
        """edge:空 list 應回傳「沒找到」"""
        data = []
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                result = func(data, 1)
                self.assertFalse(_found(result, func))

    def test_single_element_found(self):
        """edge:單一元素且目標存在"""
        data = [7]
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                result = func(data, 7)
                self.assertTrue(_found(result, func))

    def test_single_element_not_found(self):
        """edge:單一元素但目標不存在"""
        data = [7]
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                result = func(data, 1)
                self.assertFalse(_found(result, func))

    def test_duplicate_values(self):
        """edge:重複值存在,linear/binary 應回傳其中一個 index"""
        data = [4, 2, 4, 4, 2]
        sorted_data = sorted(data)
        target = 4
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                if func.__name__ == "binary_search":
                    result = func(sorted_data, target)
                else:
                    result = func(data, target)
                self.assertTrue(_found(result, func))

    def test_first_and_last_position(self):
        """edge:目標在第一個或最後一個位置"""
        data = [1, 2, 3, 4, 5]
        for func in SEARCH_FUNCTIONS:
            for target in (1, 5):
                with self.subTest(func=func.__name__, target=target):
                    result = func(data, target)
                    self.assertTrue(_found(result, func))

if __name__ == "__main__":
    unittest.main()
