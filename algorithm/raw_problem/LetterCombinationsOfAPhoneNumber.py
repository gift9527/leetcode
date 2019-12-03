# -*- coding: utf-8 -*-

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])

        remaind = self.letterCombinations(digits[:-1])
        current_element = mapping[digits[-1]]
        return [i+j for i in remaind for j in current_element]

if __name__ == "__main__":
    a = Solution()
    c = a.letterCombinations("234")
    print(c)