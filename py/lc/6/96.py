import unittest


class Solution:
    results = [1, 1, 2]

    def numTrees(self, n: int) -> int:
        return int(self.factorial(2 * n) / (self.factorial(n + 1) * self.factorial(n)))

    def factorial(self, n):
        current = len(self.results) - 1
        if n > current:
            for i in range(len(self.results), n + 1):
                self.results.append(int(self.results[i - 1] * i))
        return self.results[n]


class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().numTrees(4), 14)


if __name__ == "__main__":
    unittest.main()
