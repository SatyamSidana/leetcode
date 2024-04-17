# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, r: Optional[TreeNode], v: int, d: int) -> Optional[TreeNode]:
        c=0
        if d==1:
            cur=TreeNode(v,r,None)
            return cur
        def dfs(cur,c):
            if cur!=None:
                c+=1
                if c==d-1:
                    l=cur.left
                    r=cur.right
                    cur.left=TreeNode(v,l,None)
                    cur.right=TreeNode(v,None,r)
                else:
                    dfs(cur.left,c)
                    dfs(cur.right,c)
                c-=1
        dfs(r,c)
        return r


        