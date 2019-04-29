class Solution(object):
    def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1

        return start


if __name__ == "__main__":
    a = Solution()
    f = a.removeElement([0,1,2,2,3,0,4,2],2)
    print (f)
