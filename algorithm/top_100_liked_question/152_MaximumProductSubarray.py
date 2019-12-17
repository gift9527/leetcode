class Solution(object):
    def run(self, array):
        if len(array) == 0:
            return 0
        max_tmp = array[0]
        min_tmp = array[0]
        max_result = array[0]

        for i in range(1, len(array)):
            a = array[i] * max_tmp
            b = array[i] * min_tmp
            c = array[i]

            max_tmp = max(a, b, c)
            min_tmp = min(a, b, c)
            max_result = max(max_result, max_tmp)

        return max_result


if __name__ == "__main__":
    nums = [2, 3, -2, 4]

    a = Solution()
    b = a.run(nums)
    print(b)