class Solution(object):
    def __init__(self, nums):
        self.nums = sorted(nums)

    def kSum(self, l, r, n, target, result, results):
        if ((r - l + 1) < n) or (n < 2) or (n * self.nums[l] > target) or (n * self.nums[r] < target):
            return []

        if n == 2:
            while l < r:
                s = self.nums[l] + self.nums[r]
                if s == target:
                    results.append(result + [self.nums[l]] + [self.nums[r]])
                    l += 1
                    while (self.nums[l] == self.nums[l - 1]) and (l < r):
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1

        else:
            for i in range(l, r + 1):
                if (i == l) or (i > l and self.nums[i] != self.nums[i - 1]):
                    self.kSum(i + 1, r, n - 1, target - self.nums[i], result + [self.nums[i]], results)


if __name__ == "__main__":
    a = [-1, 0, 1, 2, -1, -4]
    n = 3
    target = 0
    result = []
    results = []

    b = Solution(a)
    b.kSum(0, len(a) - 1, n, target, result, results)
    for i in results:
        print(i)
