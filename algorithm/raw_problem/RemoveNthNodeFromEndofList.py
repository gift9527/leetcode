# !/usr/bin/python
# -*- coding: utf-8 -*-

# 该问题需要注意的是进位问题，两条链表可能长度不一致，链表的操作细节
# Definition for singly-linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


if __name__ == "__main__":
    head = a = ListNode(1)
    a.next = ListNode(2)
    a = a.next
    a.next = ListNode(3)
    a = a.next
    a.next = ListNode(4)
    a = a.next
    a.next = ListNode(5)

    # while head:
    #     print(head.val)
    #     head = head.next

    c = Solution()
    d = c.removeNthFromEnd(head = head, n = 2)

    while d:
        print(d.val)
        d = d.next
