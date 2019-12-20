class Solution(object):
    def run(self, matrix, target):
        if matrix or matrix[0]:
            rows = len(matrix)
            cols = len(matrix[0])
            row = 0
            col = cols - 1

            while True:
                if row < rows and col >= 0:
                    if matrix[row][col] == target:
                        return True
                    elif matrix[row][col] < target:
                        row += 1
                    else:
                        col -= 1
                else:
                    return False


if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    target = 20
    a = Solution()
    b = a.run(matrix,target)
    print(b)

