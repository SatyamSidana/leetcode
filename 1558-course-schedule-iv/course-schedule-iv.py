class Solution:
    def checkIfPrerequisite(self, n: int, p: List[List[int]], qe: List[List[int]]) -> List[bool]:
        v=[]
        r=[]
        for i in range (n):
            v.append([])
            for j in range (n):
                v[i].append(0)
        d=[[] for _ in range(n)]

        for i in p:
            d[i[0]].append(i[1])
        q=[]
        for i in range (len(d)):
            for j in range (len(d[i])):
                q.append(d[i][j])
                v[i][d[i][j]]=1
            while q:
                b=q.pop(0)
                for z in range (len(d[b])):
                    if v[i][d[b][z]]==0:
                        q.append(d[b][z])
                        v[i][d[b][z]]=1
        for i in qe:
            if v[i[0]][i[1]]==1:
                r.append(True)
            else:
                r.append(False)
        return r

