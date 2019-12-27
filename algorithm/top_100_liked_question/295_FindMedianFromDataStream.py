# 最大堆，最小堆实现
from heapq import *


class Solution(object):
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        heappush(self.maxHeap, -num)
        minTop = self.minHeap[0] if len(self.minHeap) > 0 else None
        maxTop = self.maxHeap[0] if len(self.maxHeap) > 0 else None

        if maxTop and minTop:

            if -maxTop > minTop or len(self.minHeap) + 1 < len(self.maxHeap):
                heappush(self.minHeap, -heappop(self.maxHeap))
            if len(self.minHeap) > len(self.maxHeap):
                heappush(self.maxHeap, -heappop(self.minHeap))

        if len(self.maxHeap) == 2 and len(self.minHeap) == 0:
            # if num > -maxTop:
            heappush(self.minHeap, -heappop(self.maxHeap))
            # else:
            #     heappush(self.minHeap, -heappop(self.maxHeap))
            #     heappush(self.maxHeap, -num)

    def findMedia(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + (-self.maxHeap[0])) / 2.0
        if len(self.maxHeap) == len(self.minHeap) + 1:
            return -self.maxHeap[0]


if __name__ == "__main__":
    a = Solution()
    a.addNum(1)
    a.addNum(2)
    print(a.findMedia())

    a.addNum(3)
    print(a.findMedia())
