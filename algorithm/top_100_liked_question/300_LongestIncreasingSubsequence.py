class Solution(object):
    def run(self,nums):
        dp = [0] * len(nums)
        for i in range(len(nums)):
            tmax = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    tmax = max(tmax,dp[j] + 1)
            dp[i] = tmax

        return max(dp)




if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    a = Solution()
    b = a.run(nums)
    print(b)