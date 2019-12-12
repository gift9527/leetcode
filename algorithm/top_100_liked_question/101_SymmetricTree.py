class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def run(self, root):
        if not root:
            return True
        return self.isSymmetric(root.left, root.right)

    def isSymmetric(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        if left.val == right.val:
            if self.isSymmetric(left.left,right.right) and self.isSymmetric(left.right,right.left):
                return True
            else:
                return False


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
