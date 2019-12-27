class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def serialize(self, root):
        vals = []
        self.ge_node(root, vals)
        return "".join(vals)

    def ge_node(self, node, vals):
        if not node:
            vals.append("#")
        else:
            vals.append(str(node.val))
            self.ge_node(node.left,vals)
            self.ge_node(node.right,vals)

    def deserialize(self, data):
        vals = list(data)
        node = self.de_node(vals)
        return node

    def de_node(self, vals):
        if vals[0] == "#":
            return None
        else:
            node = TreeNode(int(vals[0]))
            vals = vals[1:]
            if vals:
                node.left = self.de_node(vals)
            vals = vals[1:]
            if vals:
                node.right = self.de_node(vals)
            return node


if __name__ == "__main__":
    root = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(5)

    root.left = l2
    root.right = l3
    l3.left = l4
    l3.right = l5

    a = Solution()
    b = a.serialize(root)
    print(b)


    c = a.deserialize(b)
    print(1)