import unittest
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        flat_list = [item for sublist in grid for item in sublist]
        ln = len(flat_list)
        k = len(flat_list) - k
        for i in range(ln):
            grid[i // len(grid[0])][i % len(grid[0])] = flat_list[(i + k) % ln]
        return grid


class UnitTests(unittest.TestCase):
    def test_json_case1(self):
        self.assertEqual(
            Solution().shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1),
            [[9, 1, 2], [3, 4, 5], [6, 7, 8]],
        )

    def test_json_case2(self):
        self.assertEqual(Solution().shiftGrid([[]], 1), [[]])

    def test_json_case3(self):
        self.assertEqual(Solution().shiftGrid([[1, 2, 3]], 1), [[3, 1, 2]])


if __name__ == "__main__":
    unittest.main()
