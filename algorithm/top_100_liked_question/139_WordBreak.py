class Solution(object):
    def run(self, s, dict):
        DP = [False] * (len(s) + 1)
        DP[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if DP[j] and s[j:i] in dict:
                    DP[i] = True

        return DP[-1]


if __name__ == "__main__":
    s = "leetcode"
    dict = ['leet', 'code']

    a = Solution()
    b = a.run(s, dict)
    print(b)
