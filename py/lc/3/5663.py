from typing import List
import unittest


class Solution:
    def init(self):
        self.cache_x = List[List[int]]

    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        res = []
        # if len(matrix) == 1:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = matrix[i][j] ^ matrix[i - 1][j]
        for i in range(len(matrix)):
            res.append(matrix[i][0])
            for j in range(1, len(matrix[0])):
                matrix[i][j] = matrix[i][j] ^ matrix[i][j - 1]
                res.append(matrix[i][j])
        res = sorted(res, reverse=True)
        return res[k - 1]


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().kthLargestValue([[5, 2], [1, 6]], 3), 4)
        self.assertEqual(Solution().kthLargestValue([[5, 2], [1, 6]], 4), 0)
        self.assertEqual(Solution().kthLargestValue([[5, 2], [1, 6]], 2), 5)
        self.assertEqual(
            Solution().kthLargestValue(
                [[8, 10, 5, 8, 5, 7, 6, 0, 1, 4, 10, 6, 4, 3, 6, 8, 7, 9, 4, 2]], 2
            ),
            14,
        )
        self.assertEqual(Solution().kthLargestValue([[8], [10], [5]], 2), 7)


unittest.main()
