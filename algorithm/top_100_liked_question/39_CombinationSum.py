class Solution(object):
    def run(self, candidates, target):
        result = []
        candidates.sort()
        self.combination_sum(candidates, 0, target, [], result)
        return result

    def combination_sum(self, nums, l, target, res_tmp, result):
        if target < 0:
            return

        if target == 0:
            result.append(res_tmp)

        for i in range(l, len(nums)):
            self.combination_sum(nums, i, target - nums[i], res_tmp + [nums[i]], result)


if __name__ == "__main__":
    array = [2, 3, 5]
    target = 8

    a = Solution()
    s = a.run(array, target)

    print(s)
