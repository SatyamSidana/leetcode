class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[]
        for i in range (m):
            dp.append([])
            for j in range (n):
                dp[i].append(-1)
        dp[m-1][n-1]=1
        def calc(x,y):
            if x>m-1 or y>n-1:
                return 0
            if x==m-1 and y==n-1:
                return 1
            if x<m-1 and dp[x+1][y]!=-1:
                r=dp[x+1][y]
            else:
                r=calc(x+1,y)
            if y<n-1 and dp[x][y+1]!=-1:
                d=dp[x][y+1]
            else:
                d=calc(x,y+1)
            print(r,d)
            dp[x][y] = r+d
            return r+d
            print(dp)
        calc(0,0)
        return dp[0][0]
        
        