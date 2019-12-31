class Solution(object):
    def run(self, nums):
        len_, nums_ = len(nums), sorted(nums)
        if nums_ == nums:
            return 0
        l = min(i for i in range(len_) if nums[i] != nums_[i])
        r = max(i for i in range(len_) if nums[i] != nums_[i])
        return r - l + 1
