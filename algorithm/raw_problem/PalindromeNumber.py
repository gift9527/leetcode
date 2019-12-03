# -*- coding: utf-8 -*-

# 题目的要求是不能使用额外的空间，尽量减小时间复杂度

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        p, res = x, 0

        while p:
            res = res * 10 + p % 10
            p = int (p/10)

        return res == x


if __name__ == "__main__":
    a = Solution()
    b = a.isPalindrome(121)
    if b:
        print("true")
    else:
        print("false")
