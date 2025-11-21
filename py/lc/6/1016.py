import unittest


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        start = "{0:b}".format(N)
        if len(S) < len(start):
            return False

        for i in range(N - 1, 0, -1):
            if start not in S:
                return False
            start = "{0:b}".format(i)
        return True


class tests(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().queryString("0110", 3), True)
        self.assertEqual(Solution().queryString("0110", 4), False)


unittest.main()
