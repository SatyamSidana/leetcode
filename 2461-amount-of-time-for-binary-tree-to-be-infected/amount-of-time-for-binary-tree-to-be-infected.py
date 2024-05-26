# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    b=0
    def amountOfTime(self, root: Optional[TreeNode], s: int) -> int:
        q=[]
        cur=root
        def dfs(cur,e):
            if cur!=None:
                if cur.val==e:
                    self.b=cur
                else:
                    dfs(cur.left,e)
                    dfs(cur.right,e)
        def addparent(cur,prev):
            if cur!=None:
                cur.parent=prev
                a=addparent(cur.left,cur)
                b=addparent(cur.right,cur)
        addparent(root,None)
        dfs(root,s)  
        q.append(self.b)
        c=0
        while q:
            sz=len(q)
            for i in range (sz):
                b=q.pop(0)
                b.val*=-1
                if b.left and b.left.val>0 :
                    q.append(b.left)
                if b.right and b.right.val>0 :
                    q.append(b.right)
                if b.parent and b.parent.val>0 :
                    q.append(b.parent)    
            c+=1 

        return c-1   


        