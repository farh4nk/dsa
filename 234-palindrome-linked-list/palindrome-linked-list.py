# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        curr = head
        while curr:
            s.append(curr.val)
            curr = curr.next
        while head:
            if head.val != s[-1]:
                return False
            s.pop()
            head = head.next
        return True