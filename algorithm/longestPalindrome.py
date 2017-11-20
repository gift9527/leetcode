# -*- coding: utf-8 -*-

#每次增加一个字母，回文最大长度增加一或者二，判断用python的list倒序判断

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 1
        start_index = 0
        for i in xrange(len(s)):
            if i-maxlen >= 1 and s[i-maxlen-1:i+1] == s[i-maxlen-1:i+1][::-1]:
                start_index = i - maxlen - 1
                maxlen = maxlen + 2
                continue
            if i - maxlen >=0 and s[i-maxlen:i+1] == s[i-maxlen:i+1][::-1]:
                start_index = i - maxlen
                maxlen = maxlen + 1
        return s[start_index:start_index+maxlen]


if __name__ == "__main__":
    a = Solution()
    b = a.longestPalindrome("babadaba")
    print b
