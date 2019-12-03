class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        ans = []
        Dict = dict.fromkeys(L, 0)
        for word in L:
            Dict[word] = Dict[word] + 1

        totWord = len(L)
        wordLen = len(L[0])
        slen = len(S) - totWord * wordLen;
        for i in range(0, slen + 1):
            cnt = dict.fromkeys(L, 0)
            okNum = 0
            for k in range(0, totWord):
                cur = S[i + k * wordLen:i + (k + 1) * wordLen]
                if (cur in Dict):
                    cnt[cur] = cnt[cur] + 1
                    if (cnt[cur] > Dict[cur]):
                        break
                    okNum = okNum + 1

            if (okNum == totWord):
                ans.append(i)

        return ans


if __name__ == "__main__":
    S = "barfoothefoobarman"
    L = ["foo","bar"]

    a = Solution()
    k = a.findSubstring(S,L)
    print (k)