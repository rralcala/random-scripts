import unittest
from collections import Counter

"""https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/"""


class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = Counter(s)

        if s == "":
            return 0
        ret = 0
        allpass = True
        for v, c in cnt.most_common():
            if c < k:
                allpass = False

                for ns in s.split(v):
                    x = self.longestSubstring(ns, k)
                    if x > ret:
                        ret = x
                break
        if not allpass:
            return ret
        return len(s)


class Tests(unittest.TestCase):
    def testcases(self):
        o = Solution()
        self.assertEqual(o.longestSubstring("ababbacb", 3), 6)
        self.assertEqual(o.longestSubstring("", 3), 0)
        self.assertEqual(o.longestSubstring("abc", 3), 0)


if __name__ == "__main__":
    unittest.main()
