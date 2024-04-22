# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        a=[]
        def dfs(cur):
            if cur==None:
                return 0   
            l=dfs(cur.left)
            r=dfs(cur.right)
            a.append(l+r)
            return max(l,r)+1
        dfs(root)
        return max(list(a))

                