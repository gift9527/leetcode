# class Solution:
# # @return an integer
#     def divide(self, dividend, divisor):
#         positive = (dividend < 0) is (divisor < 0)
#         dividend, divisor = abs(dividend), abs(divisor)
#         res = 0
#         while dividend >= divisor:
#             temp, i = divisor, 1
#             while dividend >= temp:
#                 dividend -= temp
#                 res += i
#                 i <<= 1
#                 temp <<= 1
#         if not positive:
#             res = -res
#         return min(max(-2147483648, res), 2147483647)
#
#
# if __name__ == "__main__":
#     a = Solution()
#     s = a.divide(72,5)
#     print(s)


class Solution(object):
    def run(self, dividend, divisor):
        res = 0
        positive = (dividend < 0) is (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend > divisor:
            tmp, i = divisor, 1
            while dividend > tmp:
                dividend -= tmp
                res += i
                i << 1
                tmp << 1

        if not positive:
            res = -res

        return res


if __name__ == "__main__":
    a = Solution()
    s = a.run(0, -5)
    print(s)
