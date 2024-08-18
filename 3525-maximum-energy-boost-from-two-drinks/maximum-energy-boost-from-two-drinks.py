class Solution:
    def maxEnergyBoost(self, A: List[int], B: List[int]) -> int:
        n=len(A)
        dp=[]
        for i in range (n+1):
            dp.append([-1]*2)
        def f(i,flag):
            if i>=n:
                return 0
            if dp[i][flag]!=-1:
                return dp[i][flag]
            if i==-1:
                x=max(f(i+1,0),f(i+1,1))
                dp[i][flag]=x
                return x
            if flag==0:
                x=max(A[i]+f(i+1,0),f(i+1,1))
            else:
                x=max(B[i]+f(i+1,1),f(i+1,0))
            dp[i][flag]=x
            return x
        return f(-1,0)