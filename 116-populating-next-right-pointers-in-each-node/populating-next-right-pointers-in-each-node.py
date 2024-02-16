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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        a=[]
        q=[]
        cur=root
        if not root:
            return None
        q.append(cur)
        while q:
            b=q.pop(0)
            a.append(b)
            if b.left!=None:
                q.append(b.left)
            if b.right!=None:
                q.append(b.right)
        s=0
        while a:
            b=a.pop(0)
            m=2**s
            for i in range (m-1):
                c=a.pop(0)
                b.next=c
                b=b.next
            s+=1
        return root

                




        