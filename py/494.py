from typing import List
class Solution:

    def findTargetSumWays(self, nums: List[int], s: int) -> int:
        nums = sorted(nums, reverse=True)
        self.memo = {}
        return self._findTargetSumWays(nums, s, len(nums), 0, 0)

    def _findTargetSumWays(self, nums: List[int], s: int, depth, sum: int, i: int) -> int:
        if depth == 0:
            # print(sign)
            if s == sum:
                return 1
            else:
                return 0
        depth -= 1
        memoi = self.memo.setdefault(i, {})
        if sum in memoi:
            return memoi[sum]
        else:
            memoi[sum] = self._findTargetSumWays(nums, s, depth, sum + nums[i], i + 1) + self._findTargetSumWays(nums, s, depth, sum - nums[i], i + 1)
            return memoi[sum]
sol = Solution()
a = [1, 1, 1, 1, 1]
b = [35,25,24,23,2,47,39,22,3,7,11,26,6,30,5,34,10,43,41,28]
#print(sol.findTargetSumWays(a, 3))
print(sol.findTargetSumWays(b, 49))