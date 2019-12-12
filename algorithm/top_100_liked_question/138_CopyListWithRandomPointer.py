class RandomNode(object):
    def __init__(self, x):
        self.val = x
        self.random = None
        self.next = None


class Solution(object):
    def run(self, root):
        if root == None:
            return None

        nodeDict = {}
        copy_root = RandomNode(root.val)
        nodeDict[root] = copy_root

        p = root
        q = copy_root

        while p != None:
            q.random = p.random
            if p.next != None:
                q.next = RandomNode(p.next.val)
                nodeDict[p.next] = q.next
            else:
                q.next = None
            p = p.next
            q = q.next

        v = copy_root
        while v != None:
            if v.random != None:
                v.random = nodeDict[v.random]
            v = v.next
        return copy_root