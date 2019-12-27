class Solution(object):
    def run(self, prices):
        if prices:
            buy = [0] * len(prices)
            sell = [0] * len(prices)
            buy[0] = -prices[0]

            for i in range(1, len(prices)):
                delta = prices[i] - prices[i - 1]
                buy[i] = max(sell[i - 2] - prices[i] if i > 1 else buy[0], buy[i - 1] - delta)
                sell[i] = max(sell[i-1] + delta, buy[i-1] + prices[i])
            return max(sell)

        else:
            return 0


if __name__ == "__main__":
    prices = [1, 2, 3, 0, 2]
    a = Solution()
    b = a.run(prices)
    print(b)
