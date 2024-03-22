# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        a={}
        cur=root
        q=[]
        q.append(cur)
        while q:
            b=q.pop(0)
            if a.get(k-b.val):
                return True
            a[b.val]=1
            if b.left :
                q.append(b.left)
            if b.right:
                q.append(b.right)
        return False
        