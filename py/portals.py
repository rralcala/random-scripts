import string
from typing import Tuple, List
import unittest


def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    if R * C < 2:
        return -1
    entry: Tuple[int, int, int, bool] = (0, 0, 0, False)
    portals = {}
    has_exit = False
    for i in range(R):
        for j in range(C):
            if G[i][j] in string.ascii_lowercase:
                portal = G[i][j]
                portals.setdefault(portal, [])
                portals[portal].append((i, j))

            if G[i][j] == "S":
                entry = (i, j, int(0), bool(False))
            if G[i][j] == "E":
                has_exit = True
    if not has_exit:
        return -1
    visited = {}
    for i in range(R):
        visited[i] = {}

    cur = G[entry[0]][entry[1]]
    visit = [entry]
    loc = entry

    while cur != "E" and len(visit) > 0:
        # Visit a node
        loc = visit.pop(0)

        cur = G[loc[0]][loc[1]]
        if cur == "E":
            break

        if loc[1] in visited[loc[0]]:
            continue
        else:
            visited[loc[0]][loc[1]] = True

        if cur == "#":
            continue
        if cur in portals and not loc[3]:
            for portal in portals[cur]:
                visit.append((portal[0], portal[1], loc[2] + 1, True))

        if loc[0] > 0:
            visit.append((loc[0] - 1, loc[1], loc[2] + 1, False))
        if loc[0] < R - 1:
            visit.append((loc[0] + 1, loc[1], loc[2] + 1, False))
        if loc[1] > 0:
            visit.append((loc[0], loc[1] - 1, loc[2] + 1, False))
        if loc[1] < C - 1:
            visit.append((loc[0], loc[1] + 1, loc[2] + 1, False))

    return loc[2] if cur == "E" else -1


class Tests(unittest.TestCase):
    def test1(self):
        R = 3
        C = 4
        G = [["a", "S", ".", "b"], ["#", "#", "#", "#"], ["E", "b", ".", "a"]]
        self.assertEqual(getSecondsRequired(R, C, G), 4)

    def test2(self):
        R = 3
        C = 3
        G = [[".", "E", "."], [".", "#", "E"], [".", "S", "#"]]
        self.assertEqual(getSecondsRequired(R, C, G), 4)

    def test3(self):
        R = 0
        C = 0
        G = [[]]
        self.assertEqual(getSecondsRequired(R, C, G), -1)

    def test4(self):
        R = 1
        C = 2
        G = [["S", "#"]]
        self.assertEqual(getSecondsRequired(R, C, G), -1)

        R = 2
        C = 1
        G = [["S"], ["E"]]
        self.assertEqual(getSecondsRequired(R, C, G), 1)

        R = 3
        C = 3
        G = [["S", "#", "a"], ["b", "#", "E"], ["b", "a", "#"]]
        self.assertEqual(getSecondsRequired(R, C, G), 5)


if __name__ == "__main__":
    unittest.main()
