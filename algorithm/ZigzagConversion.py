# -*- coding: utf-8 -*-

#还是考虑字符串的游标问题
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s
        step, index = 1, 0
        L = [""]*numRows
        for i in xrange(len(s)):
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            L[index] = L[index] + s[i]
            index = index + step
        #return L
        return "".join(L)

if __name__ == "__main__":
    a = Solution()
    b = a.convert("PAYPALISHIRING",3)
    print b





