from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_list = 0
        digit_sum = 0
        result = 0
        for num in nums:
            sum_list += num
            for digit in str(num):
                digit_sum += int(digit)
            result = num - digit_sum
        return abs(sum_list - digit_sum)


assert Solution().differenceOfSum([1, 15, 6, 3]) == 9
assert Solution().differenceOfSum([1, 2, 3, 4]) == 0
