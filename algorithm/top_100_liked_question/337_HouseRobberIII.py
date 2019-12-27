class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def run(self, root):
        return self.dfs_rob(root)[0]

    def dfs_rob(self, node):
        if not node:
            return [0, 0]
        rob_L, no_rob_L = self.dfs_rob(node.left)
        rob_R, no_rob_R = self.dfs_rob(node.right)
        return [max(no_rob_L + no_rob_R + node.val, rob_L + rob_R), rob_R + rob_L]


if __name__ == "__main__":
    l3 = TreeNode(3)
    l22 = TreeNode(2)
    l23 = TreeNode(3)
    l33 = TreeNode(3)
    l31 = TreeNode(1)

    l3.left = l22
    l3.right = l23
    l22.right = l33
    l23.right = l31

    a = Solution()
    b = a.run(l3)
    print(b)
