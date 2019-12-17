class Solution(object):
    def run(self, nums):
        nums_dict = {}

        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1

        for key, value in nums_dict.items():
            if value > len(nums) // 2:
                return key


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    a = Solution()
    b = a.run(nums)
    print(b)
