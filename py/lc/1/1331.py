import unittest
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        loc = {}

        rank = sorted(list(set(arr)))
        for i in range(len(rank)):
            loc[rank[i]] = i + 1
        for i in range(len(arr)):
            arr[i] = loc[arr[i]]
        return arr


class UnitTests(unittest.TestCase):
    def test_json_cases(self):
        self.assertEqual(
            Solution().arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]),
            [5, 3, 4, 2, 8, 6, 7, 1, 3],
        )
        self.assertEqual(Solution().arrayRankTransform([100, 100, 100]), [1, 1, 1])
        self.assertEqual(Solution().arrayRankTransform([40, 10, 20, 30]), [4, 1, 2, 3])
        self.assertEqual(Solution().arrayRankTransform([1]), [1])
        self.assertEqual(Solution().arrayRankTransform([]), [])


if __name__ == "__main__":
    unittest.main()
