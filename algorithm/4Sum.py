class Solution(object):
    def __init__(self, nums):
        self.nums = sorted(nums)

    def nSortedSum(self, l, r, n, target, result, results):
        if ((r - l + 1) < n) or (n < 2) or (n * self.nums[l] > target) or (n * self.nums[r] < target):
            return

        if n == 2:
            while l < r:
                s = self.nums[l] + self.nums[r]
                if s == target:
                    results.append(result + [self.nums[r]] + [self.nums[l]])
                    l += 1
                    while l < r and self.nums[l] == self.nums[l - 1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1

        else:
            for i in range(l, r + 1):
                if i == l or (i > l and self.nums[i] != self.nums[i - 1]):
                    self.nSortedSum(i + 1, r, n - 1, target - self.nums[i], result + [self.nums[i]],results)

        return results
if __name__ == "__main__":
    a = Solution([1, 0, -1, 0, -2, 2])
    f = a.nSortedSum(0,5,4,0,[],[])
    print (f)
