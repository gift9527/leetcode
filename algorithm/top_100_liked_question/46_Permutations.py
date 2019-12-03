class Solution(object):
    def run(self, array):
        result = []
        self.dfs(array, [], result)
        return result

    def dfs(self, nums, res, result):
        if not nums:
            result.append(res)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], res + [nums[i]], result)


if __name__ == "__main__":
    array = [1, 2, 3]
    a = Solution()
    b = a.run(array)

    for i in b:
        print(i)
