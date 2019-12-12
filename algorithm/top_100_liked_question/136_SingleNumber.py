class Solution(object):
    def run(self, array):
        nums_dict = {}
        for i in array:
            nums_dict[i] = nums_dict.get(i, 0) + 1

        for key,value in nums_dict.items():
            if value == 1:
                return key


if __name__ == "__main__":
    a = [4, 1, 2, 1, 2]

    b = Solution()

    c = b.run(a)

    print(c)