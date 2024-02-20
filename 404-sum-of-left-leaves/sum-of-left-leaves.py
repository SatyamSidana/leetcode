# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        a=[]
        q=[]
        if not root:
            return None
        cur=root
        q.append(cur)
        while q:
            b=q.pop(0)
            if b.left!=None:
                q.append(b.left)
                if b.left.left==None and b.left.right==None:
                    a.append(b.left.val)
            if b.right!=None:
                q.append(b.right)
        return sum(a)
        