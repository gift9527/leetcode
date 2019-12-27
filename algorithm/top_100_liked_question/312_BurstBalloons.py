class Solution(object):
    def run(self, nums):
        new_nums = [1] + [i for i in nums if i != 0] + [1]
        dp = [[0] * len(new_nums) for _ in range(len(new_nums))]
        for k in range(2, len(new_nums)):
            for left in range(0, len(new_nums) - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                                          new_nums[left] * new_nums[i] * new_nums[right] + dp[left][i] + dp[i][right])

        return dp[0][-1]


if __name__ == "__main__":
    a = Solution()
    nums = [3, 1, 5, 8]
    b = a.run(nums)
    print(b)
