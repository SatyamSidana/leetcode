"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q=[]
        cur=root
        if not root:
            return None
        q.append((cur,0))
        a=[]
        while q:
            b=q.pop(0)
            if len(a)>b[1]:
                a[b[1]].append(b[0])
            else:
                a.append([])
                a[b[1]].append(b[0])
            if b[0].left!=None:
                q.append((b[0].left,b[1]+1))
            if b[0].right!=None:
                q.append((b[0].right,b[1]+1))
        for i in a:
            b=i.pop(0)
            for j in range (len(i)):
                c=i.pop(0)
                b.next=c
                b=b.next
        return root 

        
        