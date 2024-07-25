class Solution:
    def maxProfit(self, p: List[int]) -> int:
        dp=[]
        for i in range (len(p)):
            dp.append([-1]*2)
        def f(i,j):
            if i>len(p)-1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if j:
                x=max(-p[i]+f(i+1,0),f(i+1,1))
            else:
                x=max(p[i]+f(i+2,1),f(i+1,0))
            dp[i][j]=x
            return x
        return f(0,1)
