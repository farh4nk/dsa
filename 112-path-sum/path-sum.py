# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        remainder = targetSum - root.val

        if not root.left and not root.right:
            if remainder == 0:
                return True
        
        return self.hasPathSum(root.left, remainder) or self.hasPathSum(root.right, remainder)

