class Solution(object):
    def run(self, array):
        M = len(array)
        N = len(array[0])
        dp = [[0] * N for _ in range(M)]
        for i in range(M):
            dp[i][0] = array[i][0]
        for i in range(N):
            dp[0][i] = array[0][i]
        for i in range(1, M):
            for j in range(1, N):
                if array[i][j] == 1:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        max_list = []
        for row in dp:
            max_list.append(max(row))
        res = max(max_list)
        #res = max(max(row) for row in dp)
        return res ** 2




if __name__ == "__main__":
    array = [[1, 0, 1, 0, 0],
             [1, 0, 1, 1, 1],
             [1, 1, 1, 1, 1],
             [1, 0, 0, 1, 0]]
    a = Solution()
    b = a.run(array)
    print(b)