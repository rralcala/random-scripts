class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ax = abs(x)
        sign = x/ax
        s = str(ax)[::-1]
        x = int(s) * sign
        return x


s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
