class Soltuon(object):
    def run(self, n):
        dp = [n] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2,n+1):
            j = 1
            while j*j < i:
                dp[i] = min(dp[i],dp[i-j*j] + 1)
                j+=1
        return dp[-1]

if __name__ == "__main__":
    a = Soltuon()
    b = a.run(14)
    print(b)

