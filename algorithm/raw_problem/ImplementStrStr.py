class Solution(object):

    def run(self, haystack, needle):
        if (not haystack) or (not needle) or (len(haystack) < len(needle)):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            ok_num = 0
            for j in range(len(needle)):
                if haystack[i+j] == needle[j]:
                    ok_num += 1
                else:
                    break
            if ok_num == len(needle):
                return i
        return -1


if __name__ == "__main__":
    a = Solution()
    b = a.run("hello", "ll")
    print(b)
