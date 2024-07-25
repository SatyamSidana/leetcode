class Solution:
    def lengthOfLIS(self, n: List[int]) -> int:
        if len(n)==1:
            return 1
        dp=[]
        for i in range (len(n)):
            dp.append([-1]*len(n))
        def f(i,j):
            if len(n)==i:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if j==-1 or n[i]>n[j]:
                x=max(1+f(i+1,i),f(i+1,j))
            else:
                x= f(i+1,j)
            dp[i][j]=x
            return x
        return f(0,-1)