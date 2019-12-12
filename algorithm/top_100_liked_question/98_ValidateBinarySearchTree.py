class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 中序遍历 或者 递归 两种解法
class Solution(object):
    def inorder_run(self, root):
        inorder_list = []
        self.inord_add(root, inorder_list)

        for i in range(1, len(inorder_list)):
            if inorder_list[i - 1] < inorder_list[i]:
                return False
        return True

    def inord_add(self, root, inorder_list):

        if not root:
            return

        self.inord_add(root.left,inorder_list)
        inorder_list.append(root.val)
        self.inord_add(root.right, inorder_list)

if __name__ == "__main__":
    # [5,1,4,null,null,3,6]
    root = TreeNode(5)
    l1 = TreeNode(1)
    l4 = TreeNode(4)
    l3 = TreeNode(3)
    l6 = TreeNode(6)

    root.left = l1
    root.right = l4
    l4.left = l3
    l4.right = l6

    a = Solution()
    b = a.inorder_run(root)
    print(b)
