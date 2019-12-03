class Solution(object):

    def run(self, digits):

        phone_number_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if digits == "":
            return []

        if len(digits) == 1:
            return [x for x in phone_number_dict[digits]]

        remaind = self.run(digits[:-1])
        last_digit = digits[-1]

        return [i + j for i in remaind for j in phone_number_dict[last_digit]]



if __name__ == "__main__":
    a = Solution()
    c = a.run("234")
    print(c)