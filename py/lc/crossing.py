import unittest


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        fullpath = {"0-0": 1}
        x=0
        y = 0
        for move in path:
            if move == "N":
                x += 1
            elif move == "S":
                x -= 1
            elif move == 'E':
                y -= 1
            else:
                y += 1
            pos = f"{x}-{y}"
            if pos in fullpath:
                return True
            else:
                fullpath[pos] = 1
        return False


class TestCase(unittest.TestCase):
    def test(self):
        self.assertEquals(Solution().isPathCrossing("NES"), False)
        self.assertEquals(Solution().isPathCrossing("NESWW"), True)
        self.assertEquals(Solution().isPathCrossing("N"), False)