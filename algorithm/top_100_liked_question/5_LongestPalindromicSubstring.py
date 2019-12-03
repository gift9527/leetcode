class Solution(object):
    def run(self, s):
        max_palindromic = ""

        for i in range(len(s)):
            a = self.check_palindromic(s, i, i)

            if len(a) > len(max_palindromic):
                max_palindromic = a

            b = self.check_palindromic(s, i, i + 1)

            if len(b) > len(max_palindromic):
                max_palindromic = b

        return max_palindromic

    def check_palindromic(self, s, l, r):
        while (r < len(s)) and (l >= 0) and (s[l] == s[r]):
            l -= 1
            r += 1
        return s[l + 1:r]


if __name__ == "__main__":
    a = "babad"
    b = Solution()
    c = b.run(a)
    print(c)
