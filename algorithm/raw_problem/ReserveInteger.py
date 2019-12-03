# -*- coding: utf-8 -*-

#这道题用python数组的slice方法有点赖皮，决定用递归的方法计算，减小时间复杂度

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        nums = []
        flag = 0
        result = 0
        if x<0:
            x = -x
            flag = -1
        while x:
            x, y = divmod(x, 10)
            nums.append(y)
        for i in range(len(nums)):
            result = result + nums[i]*pow(10,len(nums)-i-1)
        if flag == 0:
            return  result
        else:
            return -result



if __name__ == "__main__":
    a = Solution()
    b = a.reverse(-198900)
    print (b)




