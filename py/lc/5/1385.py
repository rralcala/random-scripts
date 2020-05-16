from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c = 0
        for i in arr1:
            works = True
            for j in arr2:
                if abs(j - i) <= d:
                    works = False
            if works:
                c += 1
        return c


print(Solution().findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))
print(Solution().findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))
