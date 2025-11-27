# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0]) # root is always first in preorder
        i = inorder.index(preorder[0]) 
        # i = idx of root in inorder
        # everything before is left subtree, everything after is right subtree
        root.left = self.buildTree(preorder[1:1+i], inorder[0:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root
        

