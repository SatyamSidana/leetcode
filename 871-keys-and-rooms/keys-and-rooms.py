class Solution:
    def canVisitAllRooms(self, r: List[List[int]]) -> bool:
        q=[]
        for i in r[0]:
            q.append(i)
        v=[0]*len(r)
        v[0]=1
        while q:
            b=q.pop(0)
            v[b]=1
            for i in r[b]:
                if v[i]==0:
                    q.append(i)
        if v==[1]*len(r):
            return True
        return False
        