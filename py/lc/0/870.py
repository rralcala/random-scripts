class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2t = []
        for i, n in enumerate(nums2):
            nums2t.append((i, n))
        nums2s = sorted(nums2t, key=lambda x: x[1])
        nums1s = sorted(nums1)
        res = [0] * len(nums1)
        pos = len(nums1s) - 1

        pos2 = 0
        for i in range(len(nums1s)):
            if nums1s[i] > nums2s[pos2][1]:
                res[nums2s[pos2][0]] = nums1s[i]
                pos2 += 1
            else:

                res[nums2s[pos][0]] = nums1s[i]
                pos -= 1

        return res


print(Solution().advantageCount([2, 7, 11, 15], [1, 10, 4, 11]))
print(Solution().advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))
