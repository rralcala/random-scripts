from typing import List
import unittest


class Solution:

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        self.depth = 0
        self.max_depth = 0
        self.build_tree(list(seq))
        cut = self.max_depth // 2
        depth = 0
        ret = []
        if cut > 0:
            for i in range(len(seq)):
                if seq[i] == "(":
                    if depth >= cut:
                        ret.append(1)
                    else:
                        ret.append(0)
                    depth += 1

                else:

                    depth -= 1
                    if depth >= cut:
                        ret.append(1)
                    else:
                        ret.append(0)
        else:
            return [0 for _ in range(len(seq))]
        return ret

    def build_tree(self, seq):
        if len(seq) == 0:
            return
        if seq.pop(0) == "(":
            self.depth += 1
            self.build_tree(seq)
        else:
            if self.depth > self.max_depth:
                self.max_depth = self.depth

            self.depth -= 1
            self.build_tree(seq)


class tests(unittest.TestCase):
    def test1(self):
        self.assertEqual([0, 1, 1, 1, 1, 0], Solution().maxDepthAfterSplit("(()())"))

    def test2(self):
        self.assertEqual(
            [0, 0, 0, 1, 1, 0, 0, 0], Solution().maxDepthAfterSplit("()(())()")
        )

    def test3(self):
        self.assertEqual([], Solution().maxDepthAfterSplit(""))

    def test4(self):
        self.assertEqual([0, 0, 0, 0], Solution().maxDepthAfterSplit("()()"))


if __name__ == "__main__":
    unittest.main()
