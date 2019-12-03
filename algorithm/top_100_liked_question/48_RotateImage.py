class Solution(object):
    def run(self, array):
        A[:] = zip(*array[::-1])
        return A

if __name__ == "__main__":
    a = Solution()
    A = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    b = a.run(A)

    for i in b:
        print(i)