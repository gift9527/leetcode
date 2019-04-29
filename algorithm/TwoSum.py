#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
时间复杂度为O(n) 利用字典遍历一边即可
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buf_dict = {}
        result_list = []
        for i in range(len(nums)):
            if nums[i] in buf_dict:
                result_list.append([buf_dict[nums[i]],i])
            else:
                buf_dict[target-nums[i]] = i
        return result_list
                
if __name__ == "__main__":
    num_list = [1,4,6,8,9,11]
    target_num = 12
    foo = Solution()
    result = foo.twoSum(num_list,target_num)
    print (result)
