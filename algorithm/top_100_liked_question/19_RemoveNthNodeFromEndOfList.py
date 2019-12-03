class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def run(self, n, node_start):
        a = b = node_start

        for i in range(n):
            a = a.next

        if not a:
            return node_start.next

        while a.next:
            a = a.next
            b = b.next

        b.next = b.next.next

        return node_start




if __name__ == "__main__":
    a_head = a = Node(0)
    a.next = Node(1)
    a = a.next
    a.next = Node(2)
    a = a.next
    a.next = Node(3)
    a = a.next
    a.next = Node(4)
    a = a.next
    a.next = Node(5)

    b = Solution()
    c = b.run(2, a_head.next)

    while c:
        print(c.val)
        c = c.next
