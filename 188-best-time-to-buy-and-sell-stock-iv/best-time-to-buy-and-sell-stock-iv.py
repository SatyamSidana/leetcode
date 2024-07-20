class Solution:
    def maxProfit(self, k: int, p: List[int]) -> int:
        dp=[]
        for i in range (len(p)):
            dp.append([])
            for j in range (2):
                dp[i].append([-1]*(2*k))

        def f(i,j,c):
            if c==2*k:
                return 0
            if i>len(p)-1:
                return 0
            if dp[i][j][c]!=-1:
                return dp[i][j][c]
            if j==1:
                x=max(-p[i]+f(i+1,0,c+1),f(i+1,1,c))
            else:
                x=max(p[i]+f(i+1,1,c+1),f(i+1,0,c))
            dp[i][j][c]=x
            return x
        f(0,1,0)
        return f(0,1,0)