# class Solution(object):
#     def run(self, height):
#         height.append(0)
#         stack = [-1]
#         ans = 0
#         for i in range(len(height)):
#             while height[i] < height[stack[-1]]:
#                 h = height[stack.pop()]
#                 w = i - stack[-1] - 1
#                 ans = max(ans, h * w)
#             stack.append(i)
#         height.pop()
#         return ans










class Solution(object):
    def run(self, height):
        height.append(0)
        stack = [-1]
        max_area = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        height.pop()
        return max_area

if __name__ == "__main__":
    a = Solution()
    b = [2, 1, 5, 6, 2, 3]
    c = a.run(b)
    print(c)
