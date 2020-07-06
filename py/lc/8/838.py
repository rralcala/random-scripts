import unittest


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        work = {}
        ln = len(dominoes)
        for i in range(ln):
            if dominoes[i] == ".":
                work[i] = 1
        new_keys = list(work.keys())
        keys = []
        while len(new_keys) != len(keys):
            keys = new_keys
            changes = {}
            for i in keys:
                if (
                    i - 1 >= 0
                    and dominoes[i - 1] == "R"
                    and i + 1 < ln
                    and dominoes[i + 1] == "L"
                ):
                    changes[i] = ","
                    del work[i]
                elif i - 1 >= 0 and dominoes[i - 1] == "R":
                    changes[i] = "R"
                    del work[i]
                elif i + 1 < ln and dominoes[i + 1] == "L":
                    changes[i] = "L"
                    del work[i]
            for k, v in changes.items():
                dominoes[k] = v
            new_keys = list(work.keys())

        return "".join(dominoes).replace(",", ".")


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(Solution().pushDominoes(".L.R...LR..L.."), "LL.RR.LLRRLL..")
        self.assertEqual(Solution().pushDominoes("RR.L"), "RR.L")

        self.assertEqual(Solution().pushDominoes("."), ".")
        self.assertEqual(Solution().pushDominoes("...L"), "LLLL")
        self.assertEqual(Solution().pushDominoes("R..."), "RRRR")


if __name__ == "__main__":
    unittest.main()
