class Solution(object):
    def nextPermutation(self, nums):
        if len(nums) < 2:
            return False
        elif len(nums) == 2:
            return self.reverse(0, 1, nums)
        else:
            r = len(nums) - 1
            while (r - 1 > 0) and (nums[r] <= nums[r - 1]):
                r -= 1
            if r == 0:
                self.reverse(0, r, nums)
                return nums
            pviot = r - 1
            successor = 0
            for i in range(len(nums) - 1, pviot, -1):
                if nums[i] > nums[pviot]:
                    successor = i
                    break
            nums[pviot], nums[successor] = nums[successor], nums[pviot]
            self.reverse(pviot + 1, len(nums) - 1, nums)
            return nums
    def reverse(self, l, r, nums):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


if __name__ == "__main__":
    a = Solution()
    f = a.nextPermutation([1, 1, 5])
    print(f)
