class Solution(object):

    def run(self, s):

        used = {}
        start = maxlength = 0
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1

            else:
                maxlength = max(maxlength, i - start + 1)

            used[s[i]] = i
        return maxlength


if __name__ == "__main__":
    s = "abcba"

    a = Solution()
    m = a.run(s)
    print(m)
