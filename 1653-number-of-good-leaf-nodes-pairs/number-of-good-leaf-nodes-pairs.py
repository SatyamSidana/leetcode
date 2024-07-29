# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, d: int) -> int:
        a=[]
        adj=defaultdict(list)
        def dfs(cur):
            if cur==None:
                return None
            if cur.left==None and cur.right==None:
                a.append(cur) 
            if cur.left!=None:
                adj[cur].append(cur.left)
                adj[cur.left].append(cur)
            if cur.right!=None:
                adj[cur].append(cur.right)
                adj[cur.right].append(cur)
            dfs(cur.left)
            dfs(cur.right)
        def f(fix,cur,c):
            if c<0:
                return 0
            if cur.left==None and cur.right==None and cur!=fix and v[cur]==1:
                v[cur]=0
                return 1
            y=0
            for i in adj[cur]:
                y+=f(fix,i,c-1)
            return y
        dfs(root)
        if len(adj)==1:
            return 0
        ans=0
        for i in a:
            v={}
            for j in a:
                v[j]=1
            ans+=f(i,i,d)
        return ans//2