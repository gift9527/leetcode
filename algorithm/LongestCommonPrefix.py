# -*- coding: utf-8 -*-

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for index, element in enumerate(zip(*strs)):
            if len(set(element)) > 1:
                return strs[0][:index]
        return min(strs)

if __name__ == "__main__":
    a = Solution()
    print a.longestCommonPrefix([""])
