class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def run(self, rootA, rootB):
        if (not rootA) or (not rootB):
            return None

        lenA = self.len_list(rootA)
        lenB = self.len_list(rootB)

        if lenA > lenB:
            for i in range(lenA - lenB):
                rootA = rootA.next
        else:
            for i in range(lenB-lenA):
                rootB = rootB.next

        while rootA != rootB:
            rootA = rootA.next
            rootB = rootB.next

        return rootA


    def len_list(self, head):
        index = 0
        while head:
            index += 1
            head = head.next
        return index


if __name__ == "__main__":
    l4 = ListNode(4)
    l1 = ListNode(1)
    l8 = ListNode(8)
    l5 = ListNode(5)
    l7 = ListNode(7)
    l0 = ListNode(0)

    l4.next = l1
    l1.next = l8
    l8.next = l5

    l7.next = l0
    l0.next = l8

    a = Solution()
    b = a.run(l4,l7)
    if b:
        print(b.val)