# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        cur=root
        a=cur.val
        q=[]
        q.append(cur)
        while q:
            b=q.pop(0)
            if b.val!=a:
                return False
                break
            if b.left:
                q.append(b.left)
            if b.right:
                q.append(b.right)
        return True
        