# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a=[]
        def inorder(cur):
            if cur!=None:
                inorder(cur.left)
                if cur.left==None and cur.right==None:
                    a.append(cur.val)
                inorder(cur.right)
        inorder(root1)
        b=a
        a=[]
        inorder(root2)
        if b==a:
            return True
        return False        