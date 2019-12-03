#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if not s:
            return True
        for i,element in enumerate(s):
            if element == '(' or element == '[' or element == '{':
                stack.append(element)
            elif element == ')':
                if stack and stack.pop() == '(':
                    continue
                else:
                    return False
            elif element == ']':
                if stack and stack.pop() == '[':
                    continue
                else:
                    return False
            elif element == '}':
                if stack and stack.pop() == '{':
                    continue
                else:
                    return False
        if stack:
            return False
        return True

if __name__ == "__main__":
    a = Solution()
    if a.isValid("["):
        print ("true")
    else:
        print ("false")