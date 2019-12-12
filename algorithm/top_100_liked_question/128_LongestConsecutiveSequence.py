class Solution(object):
    def run(self, nums):
        max_len = 0
        nums = set(nums)

        while nums:
            n = nums.pop()
            l1 = 0
            l2 = 0
            i = n+1

            while i in nums:
                nums.remove(i)
                i += 1
                l1 +=1

            i = n -1
            while i in nums:
                nums.remove(i)
                i +=1
                l1 +=1

            max_len = max(l1+l2+1,max_len)
        return max_len

if __name__ == "__main__":
    a = [100, 4, 200, 1, 3, 2]

    b = Solution()

    c = b.run(a)
    print(c)