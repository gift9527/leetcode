class Solution(object):
    def run(self, s):
        result = ""
        for i in range(len(s)):
            # 两种情况 aba
            tmp = self.check_palindromic(s, i, i)

            if len(tmp) > len(result):
                result = tmp

            # abba

            tmp = self.check_palindromic(s, i, i + 1)

            if len(tmp) > len(result):
                result = tmp

        return result

    def check_palindromic(self, s, l, r):
        while l >= 0 and r < len(s) and s[r] == s[l]:
            l -= 1
            r += 1

        return s[l + 1:r]


if __name__ == "__main__":
    x = "axxabbc"
    a = Solution()
    b = a.run(x)

    print (b)


