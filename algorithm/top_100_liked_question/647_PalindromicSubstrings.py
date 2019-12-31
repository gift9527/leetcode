class Solution(object):
    def run(self, s):
        res = 0
        s_len = len(s)

        for i in range(s_len):
            res += 1
            count = 1
            while (i - count >= 0) and (i + count <= s_len - 1):
                if s[i - count] == s[i + count]:
                    res += 1
                    count += 1
                else:
                    break

            l = 0
            r = 1
            while (i + r <= s_len - 1) and (i - l >= 0):
                if s[i - l] == s[i + r]:
                    res += 1
                    l += 1
                    r += 1
                else:
                    break
        return res

if __name__ == "__main__":
    s = "aaa"
    a = Solution()
    b = a.run(s)
    print(b)
