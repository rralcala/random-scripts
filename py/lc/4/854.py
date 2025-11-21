import unittest


class Solution:

    def kSimilarity(self, A: str, B: str) -> int:
        stack = []
        tested = set()
        if A == B:
            return 0
        Al = list(A)
        Bl = list(B)
        for i in range(len(Al)):
            if Al[i] != Bl[i]:
                for j in range(i, len(Al)):
                    if Al[j] != Bl[j]:
                        B1 = list(Bl)
                        B1[i], B1[j] = B1[j], B1[i]
                        stack.append((B1, 1))
        while len(stack) > 0:
            tu = stack.pop(0)
            Bl = tu[0]
            c = tu[1]
            if Al == Bl:
                return c
            else:
                c += 1
                for i in range(len(Al)):
                    # print(Al)

                    if Al[i] != Bl[i]:
                        for j in range(i, len(Al)):
                            if Al[j] != Bl[j]:
                                B1 = list(Bl)

                                B1[i], B1[j] = B1[j], B1[i]
                                val = "".join(B1)
                                if val not in tested:
                                    # print(val)
                                    tested.add(val)
                                    stack.append((B1, c))


class Tests(unittest.TestCase):
    # def test1(self):
    #    self.assertEqual(2, Solution().kSimilarity("abc", "bca"))
    # def test3(self):
    #    self.assertEqual(2, Solution().kSimilarity("abac", "baca"))
    def test4(self):
        self.assertEqual(2, Solution().kSimilarity("aabc", "abca"))

    def test5(self):
        self.assertEqual(
            2, Solution().kSimilarity("abccaacceecdeea", "bcaacceeccdeaae")
        )


if __name__ == "__main__":
    unittest.main()
