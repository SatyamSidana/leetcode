class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        a=[]
        u=[]
        v=[0]*len(graph)
        def paths(g,s,n):
            v[s]=1
            u.append(s)
            for i in g[s]:
                paths(g,i,n)
            if u[-1]==n:
                a.append(list(u))
            u.pop()
        paths(graph,0,len(graph)-1)
        a=list(a)
        return a


        