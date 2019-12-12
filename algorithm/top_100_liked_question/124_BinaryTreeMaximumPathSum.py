class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def run(self, root):
        max_sum_path, single_path = self.dfs(root)
        return max_sum_path

    def dfs(self, root):
        if not root:
            return 0, 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        single_path_sum = max(left[1] + root.val, right[1] + root.val, 0)
        max_path_sum = max(left[0], right[0], left[1] + right[1] + root.val)
        return max_path_sum, single_path_sum


if __name__ == "__main__":
    root = TreeNode(-10)
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