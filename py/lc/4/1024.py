from typing import List
import unittest


class Solution:
    def __init__(self):
        self.t = -1
        self.clips = {}

    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        self.t = T
        c = 0
        for i in range(len(clips)):
            self.clips[i] = clips[i]
        while self.t > 0:
            c += 1
            self.t = self.find_next()
            if self.t == -1:
                return -1
        return c

    def find_next(self):
        min_start = self.t + 1
        found = False
        sel = -1
        for k, v in self.clips.items():
            if v[1] >= self.t:
                found = True
                min_start = min(min_start, v[0])
                sel = k
        if found:
            del self.clips[sel]
        else:
            return -1
        return min_start


class UnitTests(unittest.TestCase):
    def test_json_cases(self):
        self.assertEqual(
            Solution().videoStitching(
                [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10
            ),
            3,
        )

    def test_json_case1(self):
        self.assertEqual(
            Solution().videoStitching([[0, 6], [2, 9], [9, 10], [6, 10]], 10),
            2,
        )

    def test_json_case2(self):
        self.assertEqual(
            Solution().videoStitching([[0, 6], [0, 1], [1, 9], [6, 10]], 10),
            2,
        )


if __name__ == "__main__":
    unittest.main()
