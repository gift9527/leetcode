# class Solution:
#     # @param an integer
#     # @return a list of string
#     # @draw a decision tree when n == 2, and you can understand it!
#     def generateParenthesis(self, n):
#         if n == 0:
#             return []
#         res = []
#         self.helpler(n, n, '', res)
#         return res
#
#     def helpler(self, l, r, item, res):
#         if r < l:
#             return
#         if l == 0 and r == 0:
#             res.append(item)
#         if l > 0:
#             self.helpler(l - 1, r, item + '(', res)
#         if r > 0:
#             self.helpler(l, r - 1, item + ')', res)


class Solution(object):
    def run(self, n):
        if not n:
            return []
        res = []
        self.generateParenthesis(n, n, '', res)
        return res

    def generateParenthesis(self, l, r, item, res):

        if r < l:
            return

        if l == 0 and r == 0:
            res.append(item)

        if l > 0:
            self.generateParenthesis(l - 1, r, item + "(", res)

        if r > 0:
            self.generateParenthesis(l, r - 1, item + ")", res)


if __name__ == "__main__":
    a = Solution()
    f = a.run(3)
    print(f)
