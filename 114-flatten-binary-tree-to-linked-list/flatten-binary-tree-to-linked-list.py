# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        a=[]
        if not root or (root.left==None and root.right==None):
            return root
        def preorder(cur):
            if cur!=None:
                a.append(cur)
                preorder(cur.left)
                preorder(cur.right)
        preorder(root)
        b=list(a)
        ptr=root
        b.pop(0)
        for i in range (len(b)):
            c=b.pop(0)
            ptr.right=c
            ptr.left=None
            ptr=ptr.right
        
        
        