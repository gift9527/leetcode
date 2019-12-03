class Solution(object):
    def run(self, stairs_nums):
        step_way = self.climb(stairs_nums)

        return step_way

    def climb(self, stairs_numes):
        if stairs_numes == 1:
            return 1
        if stairs_numes == 2:
            return 2
        return self.climb(stairs_numes - 1) + self.climb(stairs_numes - 2)


if __name__ == "__main__":
    n = 4
    a = Solution()
    b = a.run(n)
    print(b)
