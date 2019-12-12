class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def run(self,root):
        fast = slow = root

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        index = 0
        while root != slow:
            index += 1
            slow = slow.next
            root = root.next

        return index



if __name__ == "__main__":
    root = Node(3)
    l2 = Node(2)
    l0 = Node(0)
    l_4 = Node(-4)

    root.next = l2
    l2.next = l0
    l0.next = l_4
    l_4.next = l2

    a = Solution()
    b = a.run(root)
    print(b)