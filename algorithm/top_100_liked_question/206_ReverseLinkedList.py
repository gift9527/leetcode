class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None



class Solution(object):
    def run(self,root):
        prev = None
        while root:
            cur = root
            root = root.next
            cur.next = prev
            prev = cur

        return prev


if __name__ == "__main__":
    a = Solution()

    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    b = a.run(l1)
    print(1)