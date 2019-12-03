class Solution(object):

    def run(self, s, L):
        if not S:
            return []
        if not L:
            return []

        result = []

        word_dict = dict.fromkeys(L, 0)
        word_len = len(L[0])

        for word in word_dict:
            word_dict[word] = 1

        for i in range(len(S) - word_len * len(L) + 1):
            cnt = dict.fromkeys(L, 0)

            ok_num = 0

            for j in range(len(L)):
                cur = s[i+j*word_len:i+(j+1)*word_len]

                if cur in word_dict:
                    cnt[cur] += 1

                    if cnt[cur] > word_dict[cur]:
                        break

                    ok_num += 1

            if ok_num == len(L):
                result.append(i)

        return result


if __name__ == "__main__":
    S = "barfoothefoobarman"
    L = ["foo", "bar"]

    a = Solution()
    k = a.run(S, L)
    print(k)
