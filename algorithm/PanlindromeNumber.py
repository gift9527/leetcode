# -*- coding: utf-8 -*-

#题目的要求是不能使用额外的空间，尽量减小时间复杂度

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False

        bit = 1

        while x / bit > 10 :
            bit = bit * 10

        while x > 0:
            if (x / bit)!= (x % 10):
                return False
            x = (x % bit) / 10
            bit = bit / 100
        return True

if __name__ == "__main__":
    a = Solution()
    b = a.isPalindrome(121)
    if b:
        print "true"
    else:
        print "false"
