from typing import List
import unittest


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Write your code here
    if len(C) < 2:
        return 0
    C.insert(0, 1)
    moves = 0
    for i in range(M):
        if C[i] == C[i + 1]:
            continue
        r = (C[i] - C[i + 1]) % N
        l = N - r
        moves += min(l, r)
    return moves


class TestAddFunction(unittest.TestCase):
    def test_positive_numbers(self):
        N = 10
        M = 4
        C = [9, 4, 4, 8]
        self.assertEqual(getMinCodeEntryTime(N, M, C), 11)

    def test_negative_numbers(self):
        N = 3
        M = 3
        C = [1, 2, 3]
        self.assertEqual(getMinCodeEntryTime(N, M, C), 2)

    def test_mixed_numbers(self):
        N = 3
        M = 2
        C = [1, 2]
        self.assertEqual(getMinCodeEntryTime(N, M, C), 1)


if __name__ == "__main__":
    unittest.main()
