from typing import List
from collections import Counter


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        c = Counter(A[0 : len(A) // 2 + 2])
        return c.most_common(1)[0][0]


print(Solution().repeatedNTimes([1, 2, 3, 3]) == 3)
print(Solution().repeatedNTimes([2, 1, 2, 5, 3, 2]) == 2)
print(Solution().repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]) == 5)
