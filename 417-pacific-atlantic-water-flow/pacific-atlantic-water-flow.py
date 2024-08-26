class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        n=len(h)
        m=len(h[0])
        p=[[False]*m for i in range (n)]
        a=[[False]*m for i in range (n)]
        def dfs(i,j,v,prev):
            if i<0 or i>=n or j<0 or j>=m or v[i][j] or h[i][j]<prev:
                return False
            v[i][j]=True
            dfs(i+1,j,v,h[i][j])
            dfs(i-1,j,v,h[i][j])
            dfs(i,j-1,v,h[i][j])
            dfs(i,j+1,v,h[i][j])
        for i in range(n):
            for j in range(m):
                if i==0:
                    dfs(i,j,p,0)
                if j==0:
                    dfs(i,j,p,0)
                if i==n-1:
                    dfs(i,j,a,0)
                if j==m-1:
                    dfs(i,j,a,0)
        ans=[]
        for i in range(n):
            for j in range(m):
                if a[i][j]&p[i][j]:
                    ans.append([i,j])
        
        return ans
