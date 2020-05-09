from collections import Counter
import unittest

"""https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/"""


class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        cnt = Counter(deck)

        if len(deck) < 2:
            return False
        if len(cnt) == 1:
            return True
        max = cnt.most_common()[0][1]
        for i in range(2, max + 1):
            valid = True
            for _, c in cnt.most_common():
                valid &= c % i == 0
            if valid:
                return True
        return False


class Tests(unittest.TestCase):
    def test_examples(self):
        o = Solution()
        self.assertTrue(o.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
        self.assertFalse(o.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))


if __name__ == "__main__":
    unittest.main()
