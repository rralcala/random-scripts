import unittest
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        if d == 1:
            return max(jobDifficulty)
        cuts = []
        for i in range(d - 2):
            cuts.append(i)
        cuts.append(len(jobDifficulty) - 1)

        return self.difficulty(jobDifficulty, cuts)

    def difficulty(self, jobDifficulty, cuts) -> int:
        diff = 0
        j = 0
        for i in cuts:
            print(f"{j}{i}")
            diff += max(jobDifficulty[j:i])
            j = i
        diff += max(jobDifficulty[j:])
        return diff


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(7, Solution().minDifficulty([6, 5, 4, 3, 2, 1], 2))

    def test2(self):
        self.assertEqual(-1, Solution().minDifficulty([9, 9, 9], 4))


unittest.main()
