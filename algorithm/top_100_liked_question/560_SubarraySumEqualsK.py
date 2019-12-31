class Solution(object):
    def run(self,nums,k):
        res = 0
        d = {}
        d[0] = 1
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            d[sum] = d.get(sum,0) + 1

            if sum -k in d:
                res += 1
        return res


if __name__ == "__main__":
    nums = [1, 2, 1, 3]
    k = 3

    a = Solution()
    b = a.run(nums, k)
    print(b)
