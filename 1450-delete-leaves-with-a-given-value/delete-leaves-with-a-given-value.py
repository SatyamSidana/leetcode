# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def delete(cur):
            if cur!=None:
                if cur.val==target and cur.left==None and cur.right==None:
                    return 1
                a=delete(cur.left)
                b=delete(cur.right)
                if(a==1):
                    cur.left=None
                if b==1:
                    cur.right=None
                if cur.val==target and cur.left==None and cur.right==None:
                    return 1
        a=delete(root)
        if(a==1):
            return None
        return root
