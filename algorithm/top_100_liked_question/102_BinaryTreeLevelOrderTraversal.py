class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def run(self, root):
        if not root:
            return []
        ans, level = [], [root]

        while level:
            ans.append([node.val for node in level])
            tmp = []
            for node in level:
                tmp.extend([node.left,node.right])

            level = [leaf for leaf in tmp if leaf]

        return ans



if __name__ == "__main__":
    # [5,1,4,null,null,3,6]
    root = TreeNode(1)
    l21 = TreeNode(2)
    l22 = TreeNode(2)
    l31 = TreeNode(3)
    l32 = TreeNode(3)
    l41 = TreeNode(4)
    l42 = TreeNode(4)

    root.left = l21
    root.right = l22
    l21.left = l31
    l21.right = l41
    l22.left = l42
    l22.right = l32

    a = Solution()
    b = a.run(root)
    print(b)
