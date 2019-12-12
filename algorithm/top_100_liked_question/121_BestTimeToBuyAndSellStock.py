class Solution(object):
    def run(self,prices):
        if prices:
            price = prices[0]
            profit = 0

            for i in prices[1:]:
                if i < price:
                    price = i

                profit = max(profit,i - price)

            return profit
        else:
            return 0


if __name__ == "__main__":
    a = [7, 1, 5, 3, 6, 4]
    d = [7,6,4,3,1]
    b = Solution()
    c = b.run(d)
    print(c)
