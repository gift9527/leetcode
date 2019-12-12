class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def run(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.run(preorder, inorder[:ind])
            root.right = self.run(preorder, inorder[ind + 1:])

            return root


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    a = Solution()
    b = a.run(preorder,inorder)

    print (1)
