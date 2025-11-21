from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = set([0])
        print(target)
        for num in nums:
            dp |= {num + t for t in dp}
            print(dp)
            if target in dp:
                return True
        return False
    
print(Solution().canPartition([1,5,11,5]))