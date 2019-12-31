import collections
class Solution(object):
    def run(self, array, target):
        array_len = len(array)
        dp = [collections.defaultdict(int) for _ in range(array_len + 1)]
        dp[0][0] = 1
        for i, num in enumerate(array):
            for sum, cnt in dp[i].items():
                dp[i + 1][sum + num] += cnt
                dp[i + 1][sum - num] += cnt
        return dp[array_len][target]



if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    s = 3
    a = Solution()
    b = a.run(nums,s)
    print(b)

