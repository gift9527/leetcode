class Solution(object):
    def removeDuplicatesfromSortedArray(self,nums):
        length = 1
        tmp = nums[0]
        for i in nums:
            if i == tmp:
                continue
            else:
                tmp = i
                length += 1

        return length


if __name__ == "__main__":
    a = Solution()
    f = a.removeDuplicatesfromSortedArray([1,1,2])
    print (f)
