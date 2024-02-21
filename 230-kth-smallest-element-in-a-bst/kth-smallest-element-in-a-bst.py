# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a=[]
        def preorder(cur):
            if cur!=None:
                
                preorder(cur.left)
                a.append(cur.val)
                preorder(cur.right)
        preorder(root)
        return a[k-1]
        