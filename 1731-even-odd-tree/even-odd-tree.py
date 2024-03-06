# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        a=[]
        s=[]
        cur=root
        a.append((cur,0))
        while a:
            b=a.pop(0)
            if b[0].val%2==b[1]%2:
                return False
            if len(s)>b[1]:
                if b[1]%2==0:
                    if b[0].val<=s[b[1]][-1]:
                        return False
                    s[b[1]][0]=b[0].val
                if b[1]%2==1:
                    if b[0].val>=s[b[1]][-1]:
                        return False
                    s[b[1]][0]=b[0].val
            else:
                s.append([])
                s[b[1]].append(b[0].val)
            
            if b[0].left:
                a.append((b[0].left,b[1]+1))
            if b[0].right:
                a.append((b[0].right,b[1]+1))
        return True

        