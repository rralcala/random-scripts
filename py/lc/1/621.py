import heapq
import unittest
from collections import Counter

"""https://leetcode.com/problems/task-scheduler"""


class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        n += 1
        time = 0
        cnt = Counter(tasks)
        work = [-x for x in cnt.values()]
        heapq.heapify(work)
        while work:
            stack = []
            c = 0
            for _ in range(n):
                if work:
                    w = heapq.heappop(work)
                    c += 1
                    if w < -1:
                        stack.append(w + 1)
            for item in stack:
                heapq.heappush(work, item)
            time += work and n or c
        return time


class Tests(unittest.TestCase):
    def test_examples(self):
        o = Solution()
        self.assertEqual(
            o.leastInterval(
                ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2
            ),
            16,
        )
        self.assertEqual(o.leastInterval(["A", "A", "A", "B", "B", "B"], 50), 104)
        self.assertEqual(
            o.leastInterval(["A", "B", "C", "D", "E", "A", "B", "C", "D", "E"], 4), 10
        )


if __name__ == "__main__":
    unittest.main()
