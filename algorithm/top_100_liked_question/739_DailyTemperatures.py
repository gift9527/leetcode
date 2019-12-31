# class Solution(object):
#     def run(self, T):
#         ans = [0] * len(T)
#         stack = []
#         for i, t in enumerate(T):
#             while stack and T[stack[-1]] < t:
#                 cur = stack.pop()
#                 ans[cur] = i - cur
#             stack.append(i)
#
#         return ans

























class Solution(object):
    def run(self,T):
        res = [0] * len(T)
        stack = []
        for i,t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                res[i] = i - cur
            stack.append(i)
        return res


if __name__ == "__main__":
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    a = Solution()
    b = a.run(T)
    print(b)
