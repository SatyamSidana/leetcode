# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=[]
        def dfs(cur,ans):
            if cur==None:
                return 0
            a=dfs(cur.left,ans)
            b=dfs(cur.right,ans)
            if a<0:
                a=0
            if b<0:
                b=0
            ans.append(cur.val+a+b)
            return cur.val+max(a,b)
        dfs(root,ans)
        return max(ans)