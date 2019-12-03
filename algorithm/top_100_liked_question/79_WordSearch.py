class Solution(object):
    def run(self, boards, word):
        m, n = len(boards), len(boards[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(i, j, word, boards):
                    return True

        return False

    def dfs(self, i, j, word, boards):
        if word[0] == boards[i][j]:
            if not word[1:]:
                return True
            # 标记下，这个坐标的字母不能重复使用
            boards[i][j] == "#"
            if i > 0 and self.dfs(i - 1, j, word[1:], boards):
                return True
            if j > 0 and self.dfs(i, j - 1, word[1:], boards):
                return True
            if (i < len(boards) - 1) and self.dfs(i + 1, j, word[1:], boards):
                return True
            if (j < len(boards[0]) - 1) and self.dfs(i, j + 1, word[1:], boards):
                return True

            boards[i][j] = word[0]
            return False

        else:
            return False


if __name__ == "__main__":
    a = Solution()
    b = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    w = "ABCCED"
    c = a.run(b, w)
    print(c)
