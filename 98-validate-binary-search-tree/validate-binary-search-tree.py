# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        a=[]
        def preorder(cur):
            if cur!=None:
                preorder(cur.left)
                a.append(cur.val)
                preorder(cur.right)
        
        preorder(root)
        print(a)
        if len(a)>1:
            for i in range (1,len(a)):
                if a[i]<=a[i-1]:
                    return False
        return True

        