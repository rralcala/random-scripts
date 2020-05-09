import unittest

"""https://leetcode.com/problems/smallest-range-i/"""


class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        r = max(A) - min(A) - 2 * K
        return r if r > 0 else 0


class Tests(unittest.TestCase):
    def test_examples(self):
        o = Solution()
        self.assertEqual(o.smallestRangeI([1, 3, 6], 3), 0)
        self.assertEqual(o.smallestRangeI([0, 10], 2), 6)
        self.assertEqual(o.smallestRangeI([1], 0), 0)


if __name__ == "__main__":
    unittest.main()
