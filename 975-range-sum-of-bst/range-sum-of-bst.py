# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        a=[]
        def sumorder(cur):
            if cur!=None:
                sumorder(cur.left)
                b=cur.val
                print(b)
                if low<=b<=high :
                    a.append(cur.val)
                sumorder(cur.right)
        sumorder(root)
        return sum(a)