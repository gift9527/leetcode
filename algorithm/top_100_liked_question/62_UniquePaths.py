class Solution(object):
    def run(self, m, n):
        robot_map = [[1 for i in range(m)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                robot_map[i][j] = robot_map[i][j - 1] + robot_map[i - 1][j]
        return robot_map[-1][-1]


if __name__ == "__main__":
    a = Solution()
    m = 7
    n = 8
    b = a.run(m, n)
    print(b)
