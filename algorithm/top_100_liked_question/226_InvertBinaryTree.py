class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def run(self, root):
        if root:
            root.left, root.right = self.run(root.right), self.run(root.left)
            return root


if __name__ == "__main__":
    l4 = TreeNode(4)
    l2 = TreeNode(2)
    l7 = TreeNode(7)
    l1 = TreeNode(1)
    l3 = TreeNode(3)
    l6 = TreeNode(6)
    l9 = TreeNode(9)

    l4.left = l2
    l4.right = l7
    l2.left = l1
    l2.right = l3
    l7.left = l6
    l7.right = l9

    a = Solution()
    b = a.run(l4)

    print(1)