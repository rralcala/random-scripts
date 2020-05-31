import unittest


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace("X", "") != end.replace("X", ""):
            return False
        s = []
        e = []
        for i in range(len(start)):
            if not (start[i] == "X" and start[i] == end[i]):
                s.append(start[i])
                e.append(end[i])

        return self._canTransform(s, e)

    def _canTransform(self, start: str, end: str) -> bool:
        ls = 0
        rs = 0
        for i in range(len(start)):
            if start[i] == "L":
                ls -= 1
                rs = 0
            elif start[i] == "R":
                rs += 1
                ls = 0
            if end[i] == "L":
                ls += 1
                rs = 0
            elif end[i] == "R":
                rs -= 1
                ls = 0
            if rs < 0 or ls < 0:
                return False

        return True


class UnitTest(unittest.TestCase):
    def test_case1(self):
        self.assertTrue(
            Solution().canTransform(
                "RXXXXXRXXLRRXXRXXXXXXXXXLXXXLXLXXRXXXXXLXXXXX",
                "XXRXXXRLXXXXXRRRXXXXXLXXLXXXXXLXXXXRXXLXXXXXX",
            )
        )

    def test_case2(self):
        self.assertTrue(Solution().canTransform("RXXLRXRXL", "XRLXXRRLX"))

    def test_case3(self):
        self.assertTrue(Solution().canTransform("RXXXXXX", "XXXXXXR"))

    def test_case4(self):
        self.assertFalse(Solution().canTransform("LXXXXXX", "XXXXXXL"))

    def test_case_silly(self):
        self.assertTrue(Solution().canTransform("X", "X"))
        self.assertFalse(Solution().canTransform("XR", "RX"))
        self.assertTrue(Solution().canTransform("L", "L"))
