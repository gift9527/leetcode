class Solution(object):
    def run(self, s):
        max_length = 0

        character = {}
        start = 0

        for i in range(len(s)):
            if s[i] not in character:
                character[s[i]] = i
            else:
                start += 1
                character[s[i]] = i
            if max_length < (i - start + 1):
                max_length = (i - start + 1)

        return max_length


if __name__ == "__main__":
    s = "abcabc"
    a = Solution()
    d = a.run(s)
    print(d)
