# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        def preorder(cur):
            if cur!=None:
                a.append(cur.val)
                preorder(cur.left)
                preorder(cur.right)
        preorder(root)
        return list(a)
        