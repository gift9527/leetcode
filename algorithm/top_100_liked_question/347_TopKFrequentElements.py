# class Solution(object):
#     def run(self,nums,k):
#         pass
import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        cntDict = collections.defaultdict(int)
        for i in nums:
            cntDict[i] += 1
        freqList = [[] for i in range(n + 1)]
        for p in cntDict:
            freqList[cntDict[p]] += p,
        ans = []
        for p in range(n, 0, -1):
            ans += freqList[p]
        return ans[:k]


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    a = Solution()
    b = a.topKFrequent(nums,k)
    print(b)