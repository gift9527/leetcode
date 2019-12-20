class Solution(object):
    def run(self, nums):
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    a = Solution()
    b = a.run(nums)
    print(nums)
