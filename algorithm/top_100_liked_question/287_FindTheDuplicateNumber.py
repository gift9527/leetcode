class Solution(object):
    def run(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (left + right) // 2
            count = 0
            for k in nums:
                if mid < k <= right:
                    count += 1
            if count > right - mid:
                left = mid + 1
            else:
                right = mid
        return right


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    a = Solution()
    b = a.run(nums)
    print(b)
