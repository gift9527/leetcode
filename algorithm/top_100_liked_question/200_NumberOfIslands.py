class Solution(object):
    def run(self, grid):
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    count += 1
        return count


    def dfs(self, array, i, j):
        # print(i)
        # print(j)
        # print(len(array))
        # print(len(array[0]))
        if i < 0 or j < 0 or i >= len(array) or j >= len(array[0]) or array[i][j] != 1:
            return

        array[i][j] = 0
        self.dfs(array, i - 1, j)
        self.dfs(array, i + 1, j)
        self.dfs(array, i, j - 1)
        self.dfs(array, i, j + 1)



if __name__ == "__main__":
    array = [[1, 1, 1, 1, 0],
             [1, 1, 0, 1, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0]]

    array2 = [[1, 1, 0, 0, 0],
              [1, 1, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 0, 0, 1, 1]]

    a = Solution()
    b = a.run(array2)
    print(b)