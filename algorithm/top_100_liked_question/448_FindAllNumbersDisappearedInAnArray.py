class Solution(object):
    def run(self, nums):
        res = []
        numset = set(nums)
        N = len(numset)
        for i in range(1, N + 1):
            if i not in numset:
                res.append(i)
        return res


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    a = Solution()
    b = a.run(nums)
    print(b)
