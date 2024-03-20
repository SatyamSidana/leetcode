"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, e: List['Employee'], id: int) -> int:
        imp=0
        a={}
        for i in range (len(e)):
            a[e[i].id]=[e[i].importance,e[i].subordinates]
        q=[]
        q.append(id)
        while q:
            c=q.pop(0)
            b=a[c]
            imp+=b[0]
            for i in b[1]:
                q.append(i)
        return imp 

        