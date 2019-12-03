# -*- coding: utf-8 -*-

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        stack = []
        result = []
        for i,element in enumerate(heights):
            if not stack:
                stack.append(element)
            elif element < stack[-1]:
                self.calculateCurrentArea(stack, element, result)
                stack.append(element)
            else:
                stack.append(element)
        self.calculateEndArea(stack,result)
        return max(result)

    def calculateCurrentArea(self, stack, element, result):
        for i, member in enumerate(stack):
            result.append((len(stack)-i)*stack[i])
            if element < member:
                stack[i] = element

    def calculateEndArea(self,stack,result):
        for i,element in enumerate(stack):
            result.append((len(stack)-i) * stack[i])

if __name__ == "__main__":
    a = Solution()
    print a.largestRectangleArea([2,1,5,6,2,3])
