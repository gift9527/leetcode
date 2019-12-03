# class Solution(object):
#     def run(self, matrix):
#         if not matrix or not matrix[0]:
#             return 0
#         n = len(matrix[0])
#         height = [0] * (n + 1)
#         ans = 0
#         for row in matrix:
#             for i in range(n):
#                 height[i] = height[i] + 1 if row[i] == '1' else 0
#             stack = [-1]
#             for i in range(n + 1):
#                 while height[i] < height[stack[-1]]:
#                     h = height[stack.pop()]
#                     w = i - 1 - stack[-1]
#                     ans = max(ans, h * w)
#                 stack.append(i)
#         return ans


class Solution(object):
    def run(self, array):
        n = len(array[0])
        max_area = 0
        height = [0] * n

        for row in array:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == "1" else 0
            height.append(0)
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
        return max_area


if __name__ == "__main__":
    array = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]

    a = Solution()
    b = a.run(array)
    print(b)
