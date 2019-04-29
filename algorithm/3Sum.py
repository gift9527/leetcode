# -*- coding: utf-8 -*-

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        if len(nums) < 3:
            return []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                    continue
            l, r = i + 1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r = r - 1
                elif s < 0:
                    l = l + 1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r-1]:
                        r = r -1
                    l = l + 1
                    r = r -1
        return result




if __name__ == "__main__":
    a = Solution()
    print (a.threeSum(
        [13, -4, 1, 3, -1, -1, 5, -11, 13, 9, 4, 7, 5, -5, -13, -4, 8, -3, 14, -4, 14, 6, 7, 11, 4, -6, -5, -9, 14, 3,
         -9, 12, -15, 0, -8, -9, 14, 4, -5, 4, -1, -15, -12, -11, -13, -9, 1, 3, -5, 0, 14, -6, 13, -1, 12, 2, 8, -7, 9,
         0, 11, 7, -11, 3, -8, -11, 1, 13, 8, 4, -5, 14, 4, -2, 11, -2, -4, -3, -14, 6, 4, 8, 7, 3, -8, 5, 12, 7, 5, -2,
         -8, -7, 13, -11, 12, 12, -7, -10, 11, -14]))
