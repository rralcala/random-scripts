import heapq
import unittest
from typing import List

"""
highest non zero count that has a number = or > to the lenght of the stream
"""


class Calculator:
    def __init__(self, channel: List):
        self.channel = [-x for x in channel if x > 0]
        heapq.heapify(self.channel)
        self.stack = []

    def calc_c(self):
        while len(self.channel) > 0:
            if -self.channel[0] > len(self.channel) + len(self.stack):
                self.stack.append(heapq.heappop(self.channel))
            else:
                break
        if len(self.channel) == 0:
            return len(self.stack)
        return min(len(self.channel) + len(self.stack), -self.channel[0])

    def add(self, x):
        heapq.heappush(self.channel, -x)
        while len(self.channel) < -self.channel[0] and len(self.stack) > 0:
            x = self.stack.pop()
            heapq.heappush(self.channel, x)
        return self.calc_c()


class UnitTest(unittest.TestCase):
    c = Calculator([0, 2, 2])

    def test0(self):
        self.assertEquals(3, Calculator([170, 3, 0, 34]).calc_c())

    def test2(self):

        self.assertEquals(2, self.c.calc_c())

    def test21(self):
        for v in [2, 2, 2, 2, 2, 2]:
            last = self.c.add(v)
        self.assertEquals(2, last)

    def test22(self):
        self.assertEquals(9, self.c.add(9))

    def test3(self):
        self.assertEquals(2, Calculator([0, 0, 0, 99999999, 3]).calc_c())


if __name__ == "__main__":
    unittest.main()
