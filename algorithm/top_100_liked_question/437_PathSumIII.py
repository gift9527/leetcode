class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def run(self, root, sum):
        if not root:
            return 0
        return self.dfs(root, sum) + self.dfs(root.left, sum) + self.dfs(root.right, sum)

    def dfs(self, root, sum):
        res = 0
        if not root:
            return res
        sum -= root.val
        if sum == 0:
            res += 1
        res += self.dfs(root.left, sum)
        res += self.dfs(root.right, sum)

        return res


if __name__ == "__main__":
    l10 = TreeNode(10)
    l5 = TreeNode(5)
    lp3 = TreeNode(-3)
    l3 = TreeNode(3)
    l2 = TreeNode(2)
    l33 = TreeNode(3)
    lp2 = TreeNode(-2)
    l1 = TreeNode(1)
    l11 = TreeNode(11)

    l10.left = l5
    l10.right = lp3
    l5.left = l3
    l5.right = l2
    l3.left = l33
    l3.right = lp2
    l2.right = l1
    lp3.right = l11

    a = Solution()
    b = a.run(l10,8)
    print(b)

