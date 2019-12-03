class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def add_two_number(self, l1, l2):
        start = n = Node(0)
        carry = 0

        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next

            if l2:
                v2 = l2.val
                l2 = l2.next

            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = Node(val)
            n = n.next

        return start.next


if __name__ == "__main__":
    astart = a = Node(2)
    a.next = Node(4)
    a = a.next
    a.next = Node(3)

    bstart = b = Node(5)
    b.next = Node(6)
    b = b.next
    b.next = Node(4)

    c = Solution()

    d = c.add_two_number(astart,bstart)

    while d:
        print(d.val)
        d = d.next

