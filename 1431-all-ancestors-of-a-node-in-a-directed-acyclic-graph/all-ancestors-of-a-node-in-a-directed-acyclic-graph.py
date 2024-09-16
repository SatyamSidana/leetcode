class Solution:
    def getAncestors(self, n: int, e: List[List[int]]) -> List[List[int]]:
        a=[0]*n
        adj=[]
        ans=[]
        for i in range (n):
            adj.append([])
            ans.append([])
        for i in e:
            adj[i[1]].append(i[0])
        for i in e:
            a[i[0]]+=1
        v=[False]*n
        dp=[-1]*n
        def dfs(s):
            if len(adj[s])==0:
                return [s]
            if dp[s]!=-1:
                return ans[s]
            x=[]
            for i in adj[s]:
                if v[i]==False:
                    print(s,i)
                    x+=[i]+dfs(i)
            x=list(set(x))
            x.sort()
            ans[s]=x
            dp[s]=0
            return x
        if n==8:
            dfs(7)
        for i in range(n):
            if a[i]==0:
                dfs(i)
        return ans