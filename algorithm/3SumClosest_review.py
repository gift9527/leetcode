class Solution(object):
    def threeSumClosest(self, nums, target):

        if len(nums) < 3:
            return []

        nums.sort()

        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                if abs(nums[i] + nums[l] + nums[r] - target) < abs(result - target):
                    result = nums[i] + nums[l] + nums[r]
                elif (nums[i] + nums[l] + nums[r]) == target:
                    return target
                elif nums[i] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return result


if __name__ == "__main__":
    a = Solution()
    m = a.threeSumClosest([0, 0, 0, 1, 1], 3)
    print(m)
