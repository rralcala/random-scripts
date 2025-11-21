from typing import List
import unittest
from functools import cache


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        surface = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                surface += self.surface(grid[i][j])
                if i > 0:
                    surface -= min(grid[i - 1][j], grid[i][j]) * 2
                if j > 0:
                    surface -= min(grid[i][j], grid[i][j - 1]) * 2
        return surface

    @cache
    def surface(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 6
        return (n - 1) * 4 + 6


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().surfaceArea([[2]]), 10)

    def test2(self):
        self.assertEqual(Solution().surfaceArea([[1, 2], [3, 4]]), 34)
        self.assertEqual(Solution().surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), 32)
        self.assertEqual(Solution().surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]), 46)


if __name__ == "__main__":
    unittest.main()
