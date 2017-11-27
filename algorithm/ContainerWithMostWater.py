# -*- coding: utf-8 -*-

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return False
        elif len(height) == 2:
            return min(height)
        else:
            i = 0
            j = len(height) - 1
            maxArea = 0
            while (j - i) != 0:
                if height[i] < height[j]:
                    if height[i] * (j - i) > maxArea:
                        maxArea = height[i] * (j - i)
                    i = i + 1 
                else:
                    if height[j] * (j - i) > maxArea:
                        maxArea = height[j] * (j - i)
                    j = j - 1

            return maxArea


if __name__ == "__main__":
    a = Solution()
    b = a.maxArea([1, 2, 3, 4, 1])
    print b
