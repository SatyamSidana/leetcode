class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        t=False
        a=[]
        b=[]
        for i in range (n):
            a.append([])
        for i in edges:
            a[i[0]].append(i[1])
            a[i[1]].append(i[0])
        v=[0]*n
        v[source]=1
        def dfs(s,d):
            for i in a[s]:
                if not v[i] :
                    v[i]=1
                    dfs(i,d)       
            if s==d:
                b.append(0)
        dfs(source,destination)
        if len(list(b))>0:
            return True
        return t
                

        