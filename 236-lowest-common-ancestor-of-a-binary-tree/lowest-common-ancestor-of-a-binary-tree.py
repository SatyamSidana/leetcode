# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=[-1]
        def dfs(cur,a,b):
            if cur!=None:
                t1=0
                t2=0
                if cur.val==a:
                    t1=1
                if cur.val==b:
                    t2=1
                x=dfs(cur.left,a,b)
                y=dfs(cur.right,a,b)
                if x!=None:
                    t1 |=x[0]
                    t2 |=x[1]
                if y!=None:
                    t1 |=y[0]
                    t2 |=y[1]
                if t1==1 and t2==1:
                    if ans[0]==-1:
                        ans[0]=cur
                return (t1,t2)
        dfs(root,p.val,q.val)
        return ans[0]


