class Solution(object):
    def run(self, s):
        letter_dict = {"2": "abc", "3": "def", "4": "ghi",
                       "5": "jkl", "6": "mno", "7": "pqrs",
                       "8": "tuv", "9": "wxyz"}
        if len(s) == 0:
            return []
        if len(s) == 1:
            return list(letter_dict[s[0]])

        remaind = self.run(s[:-1])
        current = letter_dict[s[-1]]

        return [i + j for i in remaind for j in current]





if __name__ == "__main__":
    a = Solution()
    b = a.run("234")
    print(b)
