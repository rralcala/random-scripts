class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        q = queries[0]
        nums[q[1]] = nums[q[1]] + q[0]
        res = []
        sum = 0
        for v in nums:
            if v % 2 == 0:
                sum += v
        res.append(sum)

        for i in range(1, len(queries)):
            q = queries[i]
            if nums[q[1]] % 2 == 0:
                sum -= nums[q[1]]
            nums[q[1]] = nums[q[1]] + q[0]
            if nums[q[1]] % 2 == 0:
                sum += nums[q[1]]
            res.append(sum)
        return res


print(Solution().sumEvenAfterQueries([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]))
print(Solution().sumEvenAfterQueries([3, 2], [[4, 0], [3, 0]]))
