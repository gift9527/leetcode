class Solution(object):
    def run(self, a, b):
        l = len(a) + len(b)

        if l % 2 == 1:
            return self.findKth(a, b, l // 2)
        if l % 2 == 0:
            return (self.findKth(a, b, l // 2) + self.findKth(a, b, (l - 1) // 2)) / 2

    def findKth(self, m, n, K):
        if not m:
            return n[K]

        if not n:
            return m[K]

        lm = len(m) // 2
        ln = len(n) // 2

        vm = m[lm]
        vn = n[ln]

        if lm + ln < K:
            if vm > vn:
                return self.findKth(n[ln + 1:], m, K - ln - 1)
            else:
                return self.findKth(m[lm + 1:], n, K - lm - 1)

        else:
            if vm > vn:
                return self.findKth(m[:lm], n, K)
            else:
                return self.findKth(n[:ln], m, K)


if __name__ == "__main__":
    a = [1, 3]
    b = [2, 5]

    c = Solution()
    d = c.run(a, b)
    print(d)
