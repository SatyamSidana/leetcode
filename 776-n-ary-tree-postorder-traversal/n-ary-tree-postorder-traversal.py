"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        a=[]
        def dfs(cur):
            if cur!=None:
                for i in cur.children:
                    dfs(i)
                a.append(cur.val)
        dfs(root)
        return a