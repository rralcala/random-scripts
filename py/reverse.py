class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = x/x
        x = abs(x)
        s = str(x)
        reversed(s)
        x = int(s) * sign

s = Solution()
s.reverse()