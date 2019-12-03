class Solution(object):
    def run(self, nums):
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, tmp, res):
        res.append(tmp)

        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, tmp + [nums[i]], res)


if __name__ == "__main__":
    a = Solution()
    b = [1,2,3]
    c = a.run(b)
    print(c)