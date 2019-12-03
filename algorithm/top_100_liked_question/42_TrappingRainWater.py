class Solution(object):
    def run(self, array):
        l, r = 0, len(array) - 1
        max_l = array[0]
        max_r = array[r]

        container = 0
        while l < r:
            max_l = max(array[l], max_l)
            max_r = max(array[r], max_r)

            if max_l <= max_r:
                container += max_l - array[l]
                l += 1
            else:
                container += max_r - array[r]
                r -= 1

        return container


if __name__ == "__main__":
    array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    a = Solution()
    b = a.run(array)
    print(b)
