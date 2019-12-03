class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def run(self, a, b):
        head = cur = Node(0)

        while a and b:
            if a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next
        cur.next = a or b
        return head.next


if __name__ == "__main__":
    a_head = a = Node(0)
    a.next = Node(1)
    a = a.next
    a.next = Node(2)
    a = a.next
    a.next = Node(4)

    b_head = b = Node(0)
    b.next = Node(1)
    b = b.next
    b.next = Node(3)
    b = b.next
    b.next = Node(5)


    c = Solution()

    d = c.run(a_head.next,b_head.next)

    while d:
        print(d.val)
        d = d.next