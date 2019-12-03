class Solution(object):
    def run(self, s, p):
        if p == "":
            return s == ""
        if s == "":
            if len(p) > 1 and p[1] == "*":
                return self.run(s, p[2:])
        if len(p) > 1 and p[1] == "*":
            if self.run(s,p[2:]):
                return True
            elif p[0] == s[0] or p[0] == ".":
                return self.run(s[1:],p)
            else:
                return False

        if p[0] == s[0] or p[0] == ".":
            return self.run(s[1:],p[1:])


if __name__ == "__main__":
    a = Solution()
    k = a.run("aa", "a*")
    if k:
        print("true")
    else:
        print("false")
