# -*- coding: utf-8 -*-

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = []
        nums.sort()
        if len(nums) < 3:
            return None

        result = nums[1] + nums[0] + nums[2]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                    continue
            l, r = i + 1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return target
                if abs(s-target) < abs(result-target):
                    result = s
                if s < target:
                    l = l+1
                else:
                    r = r - 1

        return result

if __name__ == "__main__":
    a = Solution()
    a.threeSumClosest([0,0,0],1)