class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def run(self, root):
        slow = fast = root

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        node = None

        while second:
            nxt = second.next
            second.next = node
            node = second
            second = nxt

        while node:
            if node.val != root.val:
                return False
            node = node.next
            root = root.next
        return True


if __name__ == "__main__":
    a = Solution()
    l1 = Node(1)
    l2 = Node(2)
    l3 = Node(2)
    #l4 = Node(2)

    l1.next = l2
    l2.next = l3
    #l3.next = l4

    b = a.run(l1)
    print(b)
