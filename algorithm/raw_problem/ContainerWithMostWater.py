# -*- coding: utf-8 -*-

class Solution(object):
    def maxArea(self, height):
        if len(height) < 2:
            return False

        max_area = 0
        i = 0
        j = len(height) - 1

        while (j - i) != 0:
            if height[i] > height[j]:
                if (j - i) * height[j] > max_area:
                    max_area = (j - i) * height[j]
                j -= 1
            else:
                if (j - i) * height[i] > max_area:
                    max_area = (j - i) * height[i]
                i += 1
        return max_area

if __name__ == "__main__":
    a = Solution()
    b = a.maxArea([1,8,6,2,5,4,8,3,7])
    print(b)
