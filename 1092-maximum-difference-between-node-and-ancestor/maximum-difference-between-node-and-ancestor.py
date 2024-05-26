# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    mi=10**6
    ma=0
    c=0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(cur):
            if cur!=None:
                if cur.left==None and cur.right==None:
                    return [min(10**6,cur.val),max(cur.val,-1)]
                a=dfs(cur.left)
                b=dfs(cur.right)
                if cur.left==None:
                    self.c=max(self.c,abs(cur.val-b[0]),abs(cur.val-b[1]))
                    print(self.c)
                    return [min(cur.val,b[0]),max(cur.val,b[1])]
                if cur.right==None:
                    self.c=max(self.c,abs(cur.val-a[0]),abs(cur.val-a[1]))
                    print(self.c)
                    return [min(cur.val,a[0]),max(cur.val,a[1])]
                mi=min(a[0],b[0])
                ma=max(a[1],b[1])
                self.c=max(self.c,abs(cur.val-mi),abs(cur.val-ma))
                print(self.c)
                return [min(mi,cur.val),max(cur.val,ma)]
        dfs(root)
        return self.c
        
        