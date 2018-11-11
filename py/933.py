import unittest

'''https://leetcode.com/problems/number-of-recent-calls/'''


class RecentCounter:

    def __init__(self):
        self.time = 0
        self.prev = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.time = t
        self.prev.insert(0, t)
        for i in range(len(self.prev)-1,-1,-1):
            if t - 3000 <= self.prev[i] <= t:
                break
            else:
                del self.prev[i]
        return len(self.prev)


class Tests(unittest.TestCase):
    def test_examples(self):
        o = RecentCounter()
        pings = [435, 3573, 4015, 4918, 5098, 5686]
        result =[o.ping(x) for x in pings]
        self.assertEqual(result, [1, 1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()


