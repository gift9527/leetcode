class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def run(self, root):
        self.res = -1
        self.diameter(root)
        return 0 if self.res == -1 else self.res - 1

    def diameter(self, node):
        if not node:
            return 0
        left = self.diameter(node.left)
        right = self.diameter(node.right)
        self.res = max(self.res, right + left + 1)
        return max(left, right) + 1



if __name__ == "__main__":
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(5)

    l1.left = l2
    l1.right = l3
    l2.left = l4
    l2.right = l5

    a = Solution()
    b = a.run(l1)
    print(b)