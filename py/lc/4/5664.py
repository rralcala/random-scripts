import unittest


class Solution:
    def minimumBoxes(self, n: int) -> int:
        if n == 1:
            return 1

        layer = 1
        player = 0
        for i in range(1, 1817):
            print(f"{player} {n}")
            if layer > n:
                return n + player
            n -= layer
            player = layer
            layer = 1 + i + layer


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().minimumBoxes(10), 6)
        self.assertEqual(Solution().minimumBoxes(4), 3)
        self.assertEqual(Solution().minimumBoxes(3), 3)
        self.assertEqual(Solution().minimumBoxes(15), 9)


unittest.main()
