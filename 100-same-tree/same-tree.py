# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a=[]
        b=[]
        def inorder(cur,prev):
            if cur and  not prev :
                return 0
            if prev and not cur:
                return 0
            if cur==None or prev==None:
                return True
            if cur.val!=prev.val:
                return False
            return inorder(cur.left , prev.left) and inorder(cur.right , prev.right)    
        return inorder(p,q)  