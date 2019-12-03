class Solution(object):
    def medianOfTwoSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.findKth(A, B, l // 2)

        if l % 2 == 0:
            return (self.findKth(A, B, l // 2) + self.findKth(A, B, l // 2 - 1)) / 2

    def findKth(self, L, M, k):
        if not L:
            return M[k]

        if not M:
            return L[k]

        li, mi = len(L) // 2, len(M) // 2

        la, ma = L[li], M[mi]

        if li + mi < k:
            if la > ma:
                return self.findKth(L, M[mi + 1:], k - mi - 1)

            else:
                return self.findKth(M, L[li + 1:], k - li - 1)

        else:
            if la > ma:
                return self.findKth(M, L[:li], k)
            else:
                return self.findKth(L, M[:mi], k)


if __name__ == "__main__":
    A = [1, 2, 3]
    B = [4, 5, 6]
    a = Solution()
    s = a.medianOfTwoSortedArrays(A, B)
    print(s)
