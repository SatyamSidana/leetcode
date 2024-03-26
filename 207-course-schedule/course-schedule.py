class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        a=[0]*n
        for i in p:
            a[i[1]]+=1
        adj = [[] for _ in range(n)]
        for edge in p:
            adj[edge[0]].append(edge[1])
        r=[]
        q=[]
        for i in range (len(a)):
            if a[i]==0:
                q.append(i)
        
        while q:
            b=q.pop(0)
            r.append(b)
            for i in adj[b]:
                a[i]-=1
                if a[i]==0:
                    q.append(i)
        if len(r)==n:
            return True
        return False
