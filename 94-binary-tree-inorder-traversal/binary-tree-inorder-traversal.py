# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        root
        a=[]
        def inorder(cur):
            if cur!=None:
                inorder(cur.left)
                a.append(cur.val)
                inorder(cur.right)
        inorder(root)
        return a
        