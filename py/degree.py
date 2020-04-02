import collections



class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(nums)
        return cnt.most_common(1)[0][0]

s = Solution()
print(s.findShortestSubArray([2,3,4,5,4,9,4]))
print(s.findShortestSubArray([2]))
print(s.findShortestSubArray([]))


