import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        d = collections.deque()
        for i in range(len(nums)):
            while d and d[-1] < nums[i]:
                d.pop()
            d.append(nums[i])
            if i > k - 1 and d[0] == nums[i - k]:
                d.popleft()
            if i >= k - 1:
                res.append(d[0])

        return res


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    a = Solution()
    b = a.maxSlidingWindow(nums, k)
    print(b)
