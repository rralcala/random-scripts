from typing import List
import unittest


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        pop = {}
        score = 0
        i = 0
        j = 0
        max_score = 0
        for v in nums:
            pop[v] = -1
        while i < len(nums):
            if pop[nums[i]] == -1:
                pop[nums[i]] = i
                score += nums[i]
                i += 1
            else:
                if score > max_score:
                    max_score = score
                pop[nums[j]] = -1
                score -= nums[j]

                j += 1
        if score > max_score:
            return score
        return max_score


class tests(unittest.TestCase):

    def test1(self):
        self.assertEqual(17, Solution().maximumUniqueSubarray([4, 2, 4, 5, 6]))

    def test2(self):
        self.assertEqual(
            8, Solution().maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5])
        )

    def test3(self):
        self.assertEqual(1, Solution().maximumUniqueSubarray([1, 1, 1]))

    def test4(self):
        self.assertEqual(1, Solution().maximumUniqueSubarray([1]))

    def test5(self):
        self.assertEqual(
            10001, Solution().maximumUniqueSubarray([10000, 1, 10000, 1, 1, 1, 1, 1, 1])
        )


if __name__ == "__main__":
    unittest.main()
