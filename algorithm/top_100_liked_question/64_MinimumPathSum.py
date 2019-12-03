class Solution(object):
    def run(self, array):
        m = len(array)
        n = len(array[0])

        for i in range(m):
            for j in range(n):
                if i - 1 < 0 and j - 1 >= 0:
                    array[i][j] = array[i][j - 1] + array[i][j]
                elif i - 1 >= 0 and j - 1 < 0:
                    array[i][j] = array[i - 1][j] + array[i][j]
                elif i - 1 < 0 and j - 1 < 0:
                    continue
                else:
                    array[i][j] = min(array[i - 1][j], array[i][j - 1]) + array[i][j]
        return array[-1][-1]


if __name__ == "__main__":
    array = [
        [1, 3, 2],
        [1, 5, 1],
        [4, 2, 1]
    ]
    a = Solution()
    b = a.run(array)
    print(b)
