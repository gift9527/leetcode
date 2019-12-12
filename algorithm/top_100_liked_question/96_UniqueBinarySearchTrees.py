# 卡塔兰数
class Solution(object):
    def run(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1

        DP = [0] * (n + 1)
        DP[0] = 1
        DP[1] = 1
        for i in range(1, n + 1):
            for j in range(i):
                DP[i] += DP[j] * DP[i - j - 1]
        return DP[n]


if __name__ == "__main__":
    a = Solution()
    b = a.run(3)
    print(b)
