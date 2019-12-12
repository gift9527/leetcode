class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def run_recursively(self, root):
        res = []
        self.run_recursively_helper(root, res)
        return res

    def run_recursively_helper(self, root, res):
        if root:
            self.run_recursively_helper(root.left, res)
            res.append(root.val)
            self.run_recursively_helper(root.right, res)

    def run_iteratively(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res


if __name__ == "__main__":
    a = [1, None, 2, 3]
    root = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    root.right = l2
    l2.left = l3

    b = Solution()
    #c = b.run_recursively(root)
    c = b.run_iteratively(root)
    print(c)

# class GenerateBinaryTree(object):
#     def __init__(self, tree_array):
#         # self.tree_array = tree_array
#         self.root = self.ge_b_tree(tree_array)
#
#     def ge_b_tree(self, array):
#         Tree_Node_List = []
#         for i in array:
#             if i != None:
#                 Tree_Node_List.append(TreeNode(i))
#             else:
#                 Tree_Node_List.append(None)
#
#         root = None
#         for i in Tree_Node_List:
