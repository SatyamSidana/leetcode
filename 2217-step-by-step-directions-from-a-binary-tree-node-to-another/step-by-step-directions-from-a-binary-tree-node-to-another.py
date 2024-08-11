# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getDirections(self, root: Optional[TreeNode], s: int, d: int) -> str:
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
        dfs(root,s,d)
        t=ans[0]
        a=[]
        b=[]
        def f(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append('L')
            if f(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if f(node.right, target, path):
                return True
            path.pop()
            return False
        f(t,s,a)
        f(t,d,b)
        ans=""
        for i in a:
            ans+="U"
        for i in b:
            ans+=i
        return ans