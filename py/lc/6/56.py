import unittest
from typing import List


class ListNode:
    start = 0
    end = 0
    next = None

    def __init__(self, v, end):
        self.start = v
        self.end = end


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x[0])
        head = ListNode(intervals[0][0], intervals[0][1])
        cur = head
        for interval in intervals[1:]:
            if self.findStart(interval, head):

                cur.next = ListNode(interval[0], interval[1])
                cur = cur.next
        cur = head
        ret = []
        while cur:

            ret.append([cur.start, cur.end])
            cur = cur.next
        return ret

    def findStart(self, new_interval, head):
        cur = head
        while cur:
            if cur.start <= new_interval[0]:
                if cur.end >= new_interval[1]:
                    return False
                elif new_interval[0] <= cur.end and new_interval[1] >= cur.end:
                    cur.end = max(cur.end, new_interval[1])
                    return False
            elif cur.start <= new_interval[1]:
                cur.start = new_interval[0]
                cur.end = max(new_interval[1], cur.end)
                return False
            cur = cur.next
        return True


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            Solution().merge([[1, 4], [5, 6]]),
            [[1, 4], [5, 6]],
        )

    def test2(self):
        self.assertEqual(
            Solution().merge([[1, 4], [0, 0]]),
            [[0, 0], [1, 4]],
        )

    def test3(self):
        self.assertEqual(
            Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )

    def test4(self):
        self.assertEqual(
            Solution().merge([[1, 4], [4, 5]]),
            [[1, 5]],
        )


if __name__ == "__main__":
    unittest.main()
