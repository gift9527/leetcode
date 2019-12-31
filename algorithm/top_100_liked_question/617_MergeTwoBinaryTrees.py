class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def run(self, node1, node2):
        if node1 and node2:
            new_node = TreeNode(node1.val + node2.val)
            new_node.left = self.run(node1.left, node2.left)
            new_node.right = self.run(node1.right, node2.right)
            return new_node
        if not node1:
            return node2
        if not node2:
            return node1


if __name__ == "__main__":
    root1 = TreeNode(1)
    l3 = TreeNode(3)
    l2 = TreeNode(2)
    l5 = TreeNode(5)

    root1.left = l3
    root1.right = l2
    l3.left = l5

    root2 = TreeNode(2)
    l11 = TreeNode(1)
    l13 = TreeNode(3)
    l4 = TreeNode(4)
    l7 = TreeNode(7)

    root2.left = l11
    root2.right = l13
    l11.right = l4
    l13.right = l7

    a = Solution()
    b = a.run(root1,root2)
    print(1)
