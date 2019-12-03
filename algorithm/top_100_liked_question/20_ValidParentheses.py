class Solution(object):
    def run(self, s):
        if not s:
            return False

        stack = [None]

        pairs = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if (c in pairs) and pairs[c] == stack[len(stack) - 1]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 1


if __name__ == "__main__":
    s = "(){}[]"
    a = Solution()
    if a.run(s):
        print('true')
    else:
        print('false')
