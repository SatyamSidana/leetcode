# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[]
        a=[]
        if not root:
            return []
        cur=root
        q.append(cur)
        c=0
        while q:
            s=len(q)
            d=[]
            while s:
                b=q.pop(0)
                d.append(b.val)
                if b.left!=None:
                    q.append(b.left)
                if b.right!=None:
                    q.append(b.right)
                s-=1
            if c==0:
                a.append(d)  
                c=1                  
            else:
                a.append(d[::-1])
                c=0
        return a

        