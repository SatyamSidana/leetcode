# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[]
        cur=root
        if not root:
            return []
        q.append((cur,0))
        a=[]
        while q:
            b=q.pop(0)
            if len(a)>b[1]:
                a[b[1]].append(b[0].val)
            else:
                a.append([])
                a[b[1]].append(b[0].val)
            if b[0].left!=None:
                q.append((b[0].left,b[1]+1))
            if b[0].right!=None:
                q.append((b[0].right,b[1]+1))
        return a
            
        