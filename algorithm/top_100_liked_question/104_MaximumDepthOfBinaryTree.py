class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def run(self, root):
        if not root:
            return 0
        return 1 + max(self.run(root.right), self.run(root.left))




if __name__ == "__main__":
    root = TreeNode(3)
    l9 = TreeNode(9)
    l20 = TreeNode(20)
    l15 = TreeNode(15)
    l7 = TreeNode(7)

    root.left = l9
    root.right = l20
    l20.left = l15
    l20.right = l7

    a = Solution()
    b = a.run(root)
    print(b)
