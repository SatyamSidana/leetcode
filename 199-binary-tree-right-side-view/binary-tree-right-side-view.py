# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        q=[]
        if not root:
            return None
        cur=root
        q.append((cur,0))
        while q:
            b=q.pop(0)
            if len(a)>b[1]:
                a[b[1]]=b[0].val
            else:
                a.append(0)
                a[b[1]]=b[0].val
            if b[0].left!=None:
                q.append((b[0].left,b[1]+1))
            if b[0].right!=None:
                q.append((b[0].right,b[1]+1))
        
        return a
            
            

        