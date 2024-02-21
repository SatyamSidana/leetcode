# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        def preorder(cur):
            if cur!=None:
                
                preorder(cur.left)
                preorder(cur.right)
                a.append(cur.val)
        preorder(root)
        return a
        