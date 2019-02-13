# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dumphead = ListNode(0)
        curr = dumphead
        carry = 0
        while l1 or l2:
            v1 = 0
            if l1:
                v1 = l1.val
            v2 = 0
            if l2:
                v2 = l2.val
            total = carry + v1 + v2
            carry = int(total / 10)
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dumphead.next

