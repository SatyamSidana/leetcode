# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.c=0
        a=[]
        def dfs(cur):
            if cur==None:
                return 0   
            l=dfs(cur.left)
            r=dfs(cur.right)
            self.c=max(self.c,l+r)
            return max(l,r)+1
        dfs(root)
        return self.c

                