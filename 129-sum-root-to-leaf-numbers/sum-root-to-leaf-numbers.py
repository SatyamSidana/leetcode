# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        a=[]
        if not root:
            return False
        b=[]
        def cal(a):
            x=len(a)-1
            c=0
            for i in a:
                c+=i*(10**x)
                x-=1
            return c
        def preorder(cur):
            if cur!=None:
                a.append(cur.val)
                preorder(cur.left)
                preorder(cur.right)
                if cur.left==None and cur.right==None :
                    y=cal(list(a))
                    b.append(y)
                a.pop()
        preorder(root)
        return sum(b)
        