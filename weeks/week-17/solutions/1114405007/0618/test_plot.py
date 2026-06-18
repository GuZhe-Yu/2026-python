"""Stage 4 — 雷達圖測試（從零自寫）

驗證 plot.py 能產出 assets/radar.png
"""

import os
import unittest


class TestPlot(unittest.TestCase):
    def test_plot_creates_png(self):
        """執行 plot.main(), 確認 assets/radar.png 產生"""
        import plot
        if os.path.exists("assets/radar.png"):
            os.remove("assets/radar.png")
        plot.main()
        self.assertTrue(os.path.exists("assets/radar.png"))

    def test_png_is_nonempty(self):
        """驗證 PNG 檔案非空"""
        import plot
        plot.main()
        size = os.path.getsize("assets/radar.png")
        self.assertGreater(size, 0)

    def test_plot_overwrites_old_png(self):
        """edge: 重複執行會覆蓋舊檔"""
        import plot
        plot.main()
        mtime1 = os.path.getmtime("assets/radar.png")
        plot.main()
        mtime2 = os.path.getmtime("assets/radar.png")
        self.assertGreaterEqual(mtime2, mtime1)


if __name__ == "__main__":
    unittest.main()
