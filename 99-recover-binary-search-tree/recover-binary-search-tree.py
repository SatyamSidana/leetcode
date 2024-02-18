# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        a=[]
        def inorder(cur):
            if cur!=None:
                inorder(cur.left)
                a.append(cur.val)
                inorder(cur.right)
        inorder(root)
        b=list(a)
        b.sort()
        c=[]
        for i in range (len(a)):
            if a[i]!=b[i]:
                c.append(a[i])
        x,y=c[0],c[1]
        def mistake(cur):
            if cur!=None:
                mistake(cur.left)
                if cur.val==x:
                    cur.val=y
                elif cur.val==y:
                    cur.val=x
                mistake(cur.right)
        mistake(root)
        return root

        