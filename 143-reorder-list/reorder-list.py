# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # fast and slow pointer to find middle of linked list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # second points to head of second list
        second = slow.next
        slow.next = None
        first = head

        # reverse the second half of the linked list
        reverse = second
        prev = None
        while reverse:
            nxt = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = nxt
        second = prev

        # merge lists
        while first and second:
            nxt1 = first.next
            nxt2 = second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2
        
        



        