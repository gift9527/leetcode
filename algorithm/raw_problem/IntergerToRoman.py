class Solution(object):

    def run(self, x):
        strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ""
        for i in range(len(nums)):
            while x >= nums[i]:
                res += strs[i]
                x -= nums[i]

            if x == 0:
                return res


if __name__ == "__main__":
    a = Solution()

    s = a.run(1221)
    print(s)
