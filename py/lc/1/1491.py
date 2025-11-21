from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salaries = sorted(salary)[1:-1]
        return sum(salaries) / len(salaries)


print(Solution().average([8000, 9000, 2000, 3000, 6000, 1000]))
