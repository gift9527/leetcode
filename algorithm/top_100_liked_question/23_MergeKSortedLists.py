class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):

    def mergeKList(self, KList):
        if not KList:
            return []
        if len(KList) == 1:
            return KList[0]

        mid = len(KList) // 2
        l = self.mergeKList(KList[:mid])
        r = self.mergeKList(KList[mid:])

        return self.mergeTwoList(l, r)

    def mergeTwoList(self, l, r):
        head = cur = Node(0)
        while l and r:
            if l.val > r.val:
                cur.next = r
                r = r.next
            else:
                cur.next = l
                l = l.next
            cur = cur.next
        cur.next = l or r
        return head.next

if __name__ == "__main__":
    a_head = a = Node(0)
    a.next = Node(1)
    a = a.next
    a.next = Node(4)
    a = a.next
    a.next = Node(5)
    a_start = a_head.next

    b_head = b = Node(0)
    b.next = Node(1)
    b = b.next
    b.next = Node(3)
    b = b.next
    b.next = Node(4)
    b_start = b_head.next

    f_head = f = Node(0)
    f.next = Node(2)
    f = f.next
    f.next = Node(6)
    f_start = f_head.next



    c = Solution()
    d = c.mergeKList([a_start,b_start,f_start])

    while d:
        print(d.val)
        d = d.next

