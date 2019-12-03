class Solution(object):
    def run(self, x):
        if x < 0:
            return False

        p, res = x, 0

        while p:
            res = res * 10 + p % 10
            p = int(p/10)

        return res == x

if __name__ == "__main__":
    a = Solution()
    b = a.run(121)
    if b:
        print("true")
    else:
        print("false")
