# -*- coding: utf-8 -*-


# 本题 用递归的方法和动态规划的思想都能解决，故两个解决方案都用

# 递归都解决方案
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == "":
            return s == ""
        if s == "":
            if len(p) > 1 and p[1] == "*":
                return self.isMatch(s, p[2:])
            else:
                return False
        if len(p) > 1 and p[1] == "*":
            if self.isMatch(s, p[2:]):
                return True
            elif s[0] == p[0] or p[0] == ".":
                return self.isMatch(s[1:], p)
            else:
                return False
        if s[0] == p[0] or p[0] == ".":
            return self.isMatch(s[1:], p[1:])
        return False


if __name__ == "__main__":
    a = Solution()
    b = a.isMatch("a", "a*")
    if b:
        print "true"
    else:
        print "false"
