# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def lex(a,b):
            i=0
            while i<len(a) and i<len(b):
                if a[i]<b[i]:
                    return a
                elif a[i]>b[i]:
                    return b
                i+=1
            if i==len(a):
                return a
            else:
                return b
            return a
        b=[]
        a=[]
        def dfs(cur,c):
            if cur!=None:
                a.append(cur.val)
                dfs(cur.left,c)
                dfs(cur.right,c)
                if cur.left==None and cur.right==None:
                    c.append(list(a[::-1]))
                a.pop()
        dfs(root,b)
        c=[26]
        for i in b:
            c=lex(c,i)
        res=""
        for i in c:
            res+=chr(ord("a")+i)
        return res
            
            