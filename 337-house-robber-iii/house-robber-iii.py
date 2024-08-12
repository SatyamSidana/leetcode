# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(cur):
            if cur!=None:
                l=dfs(cur.left)
                r=dfs(cur.right)
                if l==None and r==None:
                    return [cur.val,0]
                if l==None:
                    l=[0,0]
                if r==None:
                    r=[0,0]
                ans=max(cur.val+l[1]+r[1],l[0]+r[0])
                return [ans,l[0]+r[0]]
        a=dfs(root)
        return a[0]

                
                