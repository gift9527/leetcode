class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


# 归并排序，先把链表分成两部分 ，每部分都排序合并
class Solution(object):
    def sort_list(self, root):
        fast = slow = root
        if (not root) or (not root.next):
            return root

        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None

        return self.merge(self.sort_list(root), self.sort_list(slow))

    def merge(self, left, right):
        res = cur = ListNode(0)

        while left and right:
            if left.val < right.val:
                cur.next = left
                cur = cur.next
                left = left.next
            else:
                cur.next = right
                cur = cur.next
                right = right.next

            if right:
                cur.next = right
            if left:
                cur.next = left


        return res.next




if __name__ == "__main__":
    l4 = ListNode(4)
    l2 = ListNode(2)
    l1 = ListNode(1)
    l3 = ListNode(3)

    l4.next = l2
    l2.next = l1
    l1.next = l3

    a = Solution()

    c = a.sort_list(l4)
    print(1)
