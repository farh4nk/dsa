# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        curr = head
        while curr:
            if visited.get(curr, False) == True:
                return True
            visited[curr] = True
            curr = curr.next
        return False