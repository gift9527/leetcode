class Solution(object):
    def run(self, array):
        d = {}

        for str in array:
            s = "".join(sorted(str))

            if s in d:
                d[s].append(str)
            else:
                d[s] = [str]

        return [d[s] for s in d]


if __name__ == "__main__":
    array = ["eat", "tea", "tan", "ate", "nat", "bat"]

    a = Solution()

    b = a.run(array)

    print(b)


