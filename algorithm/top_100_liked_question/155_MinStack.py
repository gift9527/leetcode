class Solution(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def pop(self):
        top = self.stack[-1]
        self.stack.pop()
        if top == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

    def push(self, x):
        self.stack.append(x)
        if (len(self.min_stack) == 0) or (self.min_stack[-1] > x):
            self.min_stack.append(x)



if __name__ == "__main__":
    a = Solution()
    a.push(-2)
    a.push(0)
    a.push(-3)
    print(a.getMin())
    a.pop()
    print(a.top())