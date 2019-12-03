class Solution(object):
    def run(self, word1, word2):
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        if word1[0] == word2[0]:
            return self.run(word1[1:], word2[1:])

        insert = 1 + self.run(word1, word2[1:])
        remove = 1 + self.run(word1[1:], word2)
        replace = 1 + self.run(word1[1:], word2[1:])

        return min(insert, remove, replace)


if __name__ == "__main__":
    word1 = "intention"
    word2 = "execution"

    a = Solution()
    b = a.run(word1, word2)
    print(b)
