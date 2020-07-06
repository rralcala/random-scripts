from typing import List
import unittest
import heapq


class Worker:
    def __init__(self, wage: float, quality: float):
        self.wage = wage
        self.quality = quality
        self.ratio = wage / quality

    def __str__(self) -> str:
        return f"R {self.ratio} W {self.wage} Q {self.quality}"


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], K: int
    ) -> float:
        workers = [Worker(wage[i], quality[i]) for i in range(len(wage))]
        workers.sort(key=lambda x: x.ratio)

        quality = []
        total_quality = 0.0
        total_cost = float("inf")
        for w in workers:
            total_quality += w.quality
            heapq.heappush(quality, -w.quality)

            if len(quality) > K:
                total_quality += heapq.heappop(quality)
            if len(quality) == K:
                total_cost = min(total_cost, w.ratio * total_quality)
        return total_cost


class UnitTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            105.0, Solution().mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2)
        )

    def test2(self):
        self.assertEqual(
            30.666666666666664,
            Solution().mincostToHireWorkers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3),
        )
