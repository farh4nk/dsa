# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if only one node in list
        if not head.next:
            return None
            
        l = head
        r = l
        while n > 0:
            r = r.next
            n -= 1

        # if node to be removed is first in list
        if not r:
            return head.next
        while r.next:
            l = l.next
            r = r.next
        nxt = l.next.next
        l.next = nxt
        return head