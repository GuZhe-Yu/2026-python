"""Stage 5 — 安全性測試（從零自寫）

對照 OpenSSF Secure Coding Guide，找出 ≥3 條適用規則撰寫紅燈測試。
"""

import unittest


class TestSecurity(unittest.TestCase):

    # ── pyscg-0034: Check for None Values (08 Coding Standards) ──
    def test_binary_search_explicitly_checks_none_data(self):
        """binary_search 應在入口明確檢查 None data 並提供說明訊息"""
        from search import binary_search
        with self.assertRaises(TypeError) as ctx:
            binary_search(None, 5)
        self.assertIn("data must not be None", str(ctx.exception))

    def test_binary_search_explicitly_checks_none_target(self):
        """binary_search 應在入口明確檢查 None target 並提供說明訊息"""
        from search import binary_search
        with self.assertRaises(TypeError) as ctx:
            binary_search([1, 2, 3], None)
        self.assertIn("target must not be None", str(ctx.exception))

    # ── pyscg-0014: Use Specific Exception Types (05 Exception Handling) ──
    def test_timing_no_broad_except(self):
        """timing.py 不應使用 except Exception（過度寬泛）"""
        import ast
        import timing
        with open(timing.__file__) as f:
            tree = ast.parse(f.read())
        found_broad_except = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ExceptHandler):
                if node.type is None:
                    found_broad_except = True
                elif isinstance(node.type, ast.Name) and node.type.id == "Exception":
                    found_broad_except = True
        self.assertFalse(found_broad_except, "timing.py 包含 except Exception 或 bare except")

    # ── pyscg-0051: Release Unused Resources (08 Coding Standards) ──
    def test_plot_guarantees_figure_close_on_error(self):
        """plot.py savefig 失敗時仍應確保 plt.close 被呼叫（try/finally）"""
        import inspect
        import plot
        source = inspect.getsource(plot.main)
        self.assertIn("try", source, "應使用 try/finally 確保 figure 關閉")
        self.assertIn("finally", source, "應使用 try/finally 確保 figure 關閉")


if __name__ == "__main__":
    unittest.main()
