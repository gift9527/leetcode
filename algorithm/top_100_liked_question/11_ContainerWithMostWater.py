class Solution(object):
    def run(self, array):
        if len(array) < 2:
            return False
        l, r = 0, len(array) - 1
        max_area = 0

        while l < r:
            if (max(array[l], array[r]) * (r - l) > max_area):
                max_area = min(array[l], array[r]) * (r - l)
            if array[l] > array[r]:
                r -= 1
            else:
                l += 1
        return max_area


if __name__ == "__main__":
    a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    b = Solution()
    c = b.run(a)
    print(c)
