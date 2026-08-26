# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, path=None):
            if node is None:
                return False

            if path is None:
                path = []

            path.append(node.val)    

            if not node.left and not node.right:
                res = sum(path) == targetSum
                path.pop()
                return res
            
            found = dfs(node.left, path) or dfs(node.right, path)
            path.pop()
            return found
        
        return dfs(root)

