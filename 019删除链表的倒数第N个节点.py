# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution2:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        nextNode = dummy
        secondNode = dummy

        for i in range(1, n + 2):
            nextNode = nextNode.next

        while nextNode:
            nextNode = nextNode.next
            secondNode = secondNode.next
        secondNode.next = secondNode.next.next
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        i = 0
        nextNode = dummy
        secondNode = dummy
        while True:
            if not nextNode.next:
                break
            i += 1
            nextNode = nextNode.next
            if i > n:
                secondNode = secondNode.next

        secondNode.next = secondNode.next.next
        return dummy.next

head = ListNode(1)
print(Solution().removeNthFromEnd(head, 1))