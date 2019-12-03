class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def run(self, a, b):
        head = cur = Node(0)
        carry = 0

        while a or b or carry:
            va = vb = 0
            if a:
                va = a.val
                a = a.next

            if b:
                vb = b.val
                b = b.next

            carry, val = divmod(va + vb + carry, 10)

            cur.next = Node(val)
            cur = cur.next
        return head.next

if __name__ == "__main__":
    a_head = a = Node(0)
    a.next = Node(2)
    a = a.next
    a.next = Node(4)
    a = a.next
    a.next = Node(3)

    b_head = b = Node(0)
    b.next = Node(5)
    b = b.next
    b.next = Node(6)
    b = b.next
    b.next = Node(4)

    c = Solution()
    d = c.run(a_head.next, b_head.next)

    while d:
        print(d.val)
        d = d.next
