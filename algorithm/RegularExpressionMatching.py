# -*- coding: utf-8 -*-


# 本题 用递归的方法和动态规划的思想都能解决，故两个解决方案都用

# 递归都解决方案
class SolutionA(object):
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

'''
class SolutionA(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        DP = [False * (len(p) + 1)]*(len(s)+1)
        DP[0][0] = True
        for i in xrange(1,len(p)+1):
            if p[i] == "*":
                DP[i+1][0] = DP[i-1][0]
        for i in xrange(1,len(p)+1):
            for j in xrange(1,len(s)+1):
                if p[i] == "*":
                    DP[i+i][j] = DP[i-1][j]
                elif s[i] == p[i] or p[i] == ".":
                    DP[i+1][j+1] = DP[i][j]
'''


if __name__ == "__main__":
    a = SolutionA()
    b = a.isMatch("aa", "a*")
    if b:
        print "true"
    else:
        print "false"
