class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        c=len(cuts)
        cuts = [0] + cuts + [n]
        cuts.sort()
        dp=[]
        for i in range(c+1):
            dp.append([-1]*(c+1))
        def f(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            ma=float('inf')
            for ind in range(i,j+1):
                x=cuts[j+1]-cuts[i-1]+f(i,ind-1)+f(ind+1,j)
                ma=min(ma,x)
            dp[i][j]=ma
            return ma
        return f(1,c)