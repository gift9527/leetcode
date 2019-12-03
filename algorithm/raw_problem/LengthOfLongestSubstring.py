#!/usr/bin/python
# -*- coding: utf-8 -*-


#时间复杂度是O(n),问题的关键是记录出现重复字符的索引，判断历史长度和当前索引与重复字符+1位置的长度谁大
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used_character = {}
        maxlength = 0
        current_index = 0
        for i in xrange(len(s)):
            if s[i] in used_character:
                maxlength = max(maxlength, i - current_index)
                current_index = max(current_index, used_character[s[i]] + 1)
            used_character[s[i]] = i
        return  max(maxlength, len(s)-current_index)
    
if __name__ == "__main__":
    a = Solution()
    b = a.lengthOfLongestSubstring("abcabccc")
    print b