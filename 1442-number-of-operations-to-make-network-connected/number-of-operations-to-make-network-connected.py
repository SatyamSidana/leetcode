class Solution:
    def makeConnected(self, n: int, c: List[List[int]]) -> int:
        if len(c)<n-1:
            return -1
        p=[i for i in range(n)]
        rank=[0]*n
        def find(x):
            if x==p[x]:
                return x
            else:
                return find(p[x])
        def union(x,y):
            xr=find(x)
            yr=find(y)
            if xr==yr:
                return None
            if rank[xr]>rank[yr]:
                p[yr]=xr
            elif rank[yr]>rank[xr]:
                p[xr]=yr
            else:
                p[yr]=xr
                rank[xr]+=1
        for u,v in c:
            union(u,v)
        a=0
        print(p)
        for i in range(n):
            if i==p[i]:
                a+=1
        print(a)
        return a-1