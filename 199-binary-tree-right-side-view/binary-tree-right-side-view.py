# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:


    def helper(self, node: List[TreeNode]) -> List[TreeNode]:
    # go from input level of nodes to the next level of nodes
        res = []
        for r in node:
            if r.left != None:
                res.append(r.left)
            if r.right != None:
                res.append(r.right)
        return res




    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []


        res = []
        cur_layer = [root]
        while cur_layer:
            next_layer = self.helper(cur_layer)
            res.append(cur_layer[-1].val)
            cur_layer = next_layer
        return res


