from functools import cache
import unittest


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        max = 0
        for i in range(n + 1):
            val = self.array(i)
            if val > max:
                max = val
        return max

    @cache
    def array(self, n: int):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n % 2 == 0:
            return self.array(n // 2)

        if n % 2 == 1:
            n = n // 2
            return self.array(n) + self.array(n + 1)


class tests(unittest.TestCase):

    def test1(self):
        self.assertEqual(Solution().getMaximumGenerated(7), 3)

    def test2(self):
        self.assertEqual(Solution().getMaximumGenerated(2), 1)

    def test3(self):
        self.assertEqual(Solution().getMaximumGenerated(3), 2)


unittest.main()
