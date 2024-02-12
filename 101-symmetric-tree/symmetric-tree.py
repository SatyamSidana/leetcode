# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        a=[]
        q=[]
        cur=root
        q.append(cur)
        c=0
        while q:
            m=len(q)
            x=m
            a=[]
            while m and q:
                b=q.pop(0)
                if b.left==None:
                    if len(a)>=x:
                        x-=1
                        if a.pop()!=-101:
                            return False
                    else:
                        a.append(-101)
                if b.left!=None:
                    q.append(b.left)
                    if len(a)>=x:
                        x-=1
                        if a.pop()!=b.left.val:
                            return False
                    else:
                        a.append(b.left.val)    
                if b.right==None:
                    if len(a)>=x:
                        x-=1
                        if a.pop()!=-101:
                            return False
                    else:
                        a.append(-101)
                if b.right!=None:
                    q.append(b.right)
                    if len(a)>=x:
                        x-=1
                        if a.pop()!=b.right.val:
                            return False
                    else:
                        a.append(b.right.val)
                m-=1
                print(a)
            c+=1
        return True

        