# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def len(self, head: ListNode) -> int:
        c = 0
        while head:
            c += 1
            head = head.next
        return c

    def advance(self, head: ListNode, n) -> ListNode:
        while head and n > 0:
            head = head.next
            n -= 1
        return head

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        lna = self.len(headA)
        lnb = self.len(headB)
        if lna > lnb:
            headA = self.advance(headA, lna - lnb)
        elif lnb > lna:
            headB = self.advance(headB, lnb - lna)
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
