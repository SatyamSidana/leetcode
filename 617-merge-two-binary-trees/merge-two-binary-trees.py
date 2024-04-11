# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        def dfs(a,b):
            if a==None:
                return b
            if b==None:
                return a
            a.val+=b.val
            a.left=dfs(a.left,b.left)
            a.right=dfs(a.right,b.right)
            return a
        dfs(root1,root2)
        return root1
            