# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        s=[]
        q=[]
        cur=root
        q.append((cur,0))
        while q:
            b=q.pop(0)
            if len(s)<=b[1]:
                s.append(b[0].val)
            if b[0].left:
                q.append((b[0].left,b[1]+1))
                
            if b[0].right:
                q.append((b[0].right,b[1]+1))
        return s[-1]
        