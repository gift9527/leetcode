class Solution(object):

    def run(self, A, B):

        l = len(A) + len(B)

        if l % 2 == 0:
            return (self.findKth(A, B, l // 2) + self.findKth(A, B, l // 2 - 1)) / 2

        elif l % 2 == 1:
            return self.findKth(A, B, l // 2)

    def findKth(self, M, N, k):
        if not M:
            return N[k]

        if not N:
            return M[k]

        mi, ni = len(M) // 2, len(N) // 2
        ma, na = M[mi], N[ni]

        if mi + ni < k:
            if ma > na:
                return self.findKth(N[ni + 1:], M, k - ni - 1)
            else:
                return self.findKth(N, M[mi + 1:], k - mi - 1)

        else:
            if ma > na:
                return self.findKth(N, M[:mi], k)
            else:
                return self.findKth(M, N[:ni], k)


if __name__ == "__main__":
    a = [1, 2]
    b = [3, 4]

    c = Solution()

    d = c.run(a, b)
    print(d)
