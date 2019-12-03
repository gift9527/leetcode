class Solution(object):
    def run(self, x):
        flag = 0
        result = 0
        nums = []
        if x < 0:
            x = -x
            flag = -1

        while x:
            x, y = divmod(x, 10)
            nums.append(y)

        for i in range(len(nums)):
            result = result + nums[i] * pow(10, len(nums) - i - 1)

        if flag == 0:
            return result
        else:
            return -result



if __name__ == "__main__":
    a = 1990
    b = Solution()
    c = b.run(a)
    print (c)
