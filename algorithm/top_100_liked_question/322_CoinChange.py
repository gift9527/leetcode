class Solution(object):
    def run(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        if dp[amount] == amount + 1:
            return -1
        return dp[amount]

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11

    a = Solution()
    b = a.run(coins, amount)
    print(b)
