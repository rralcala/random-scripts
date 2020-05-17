import json
from typing import List
import unittest


# TODO: Mergesort
class Solution:
    def __init__(self):
        self.lower = 0
        self.upper = 0

    def check(self, value):
        return self.lower <= value <= self.upper

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.lower = lower
        self.upper = upper
        ln = len(nums)
        c = 0
        new_partials = {}
        w = 1
        for i in range(ln):
            w += 1
            new_partials[i] = nums[i]
            if self.check(nums[i]):
                c += 1
        partials = new_partials

        while len(partials) > 0:
            new_partials = {}
            for i, s in partials.items():
                w += 1
                if i + 1 < ln:
                    new_partials[i + 1] = s + nums[i + 1]
                    if self.check(new_partials[i + 1]):
                        c += 1
            partials = new_partials
        print(w)
        return c


class UnitTests(unittest.TestCase):
    def test_json_cases(self):
        self.assertEqual(Solution().countRangeSum([-2, 7, -4, 3, 5, -1], -2, 2), 4)
        self.assertEqual(Solution().countRangeSum([-2, 5, -1], -2, 2), 3)
        self.assertEqual(Solution().countRangeSum([], -2, 2), 0)
        self.assertEqual(Solution().countRangeSum([-3], -2, 2), 0)
        with open("327-1.json") as f:
            tc = json.load(f)
            self.assertEqual(Solution().countRangeSum(*tc["params"]), tc["expected"])


if __name__ == "__main__":
    unittest.main()
