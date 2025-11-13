# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: # an empty tree is a subtree
            return True
        elif not root: # but an empty tree cannot have any subtrees
            return False
        if self.same(root, subRoot): # check if they're the same
            return True
        # if not, recursively check if either side of the main tree contains the subtree
        else: 
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same(self, p, q):
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False
        else:
            return self.same(p.left, q.left) and self.same(p.right, q.right)