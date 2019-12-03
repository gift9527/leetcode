 #!/usr/bin/python
# -*- coding: utf-8 -*-

#该问题需要注意的是进位问题，两条链表可能长度不一致，链表的操作细节
# Definition for singly-linked list.

#example
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry , val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return start.next
    
if __name__ == "__main__":
    a_start = a = ListNode(2)
    a.next = ListNode(4)
    a = a.next
    a.next = ListNode(3)


    b_start = b = ListNode(5)
    b.next = ListNode(6)
    b = b.next
    b.next = ListNode(4)

    c = Solution()
    d = c.addTwoNumbers(a_start,b_start)

    while d:
        print (d.val)
        d = d.next




            