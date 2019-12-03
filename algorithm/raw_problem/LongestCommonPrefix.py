# -*- coding: utf-8 -*-

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

if __name__ == "__main__":
    a = Solution()
    print(a.longestCommonPrefix(["flower","floor","for"]))
