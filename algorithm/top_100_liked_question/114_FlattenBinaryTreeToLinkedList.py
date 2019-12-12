class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def run(self, root):
        return self.flatten_recu(root, None)

    def flatten_recu(self, root, flatten_head):
        if root:
            flatten_head = self.flatten_recu(root.right, flatten_head)
            flatten_head = self.flatten_recu(root.left, flatten_head)

            root.right = flatten_head
            root.left = None
            return root


        else:
            return flatten_head
