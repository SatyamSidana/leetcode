class Solution:
    ans=0
    def numDistinct(self, t1: str, t2: str) -> int:
        dp=[]
        for i in range (len(t1)):
            dp.append([-1]*len(t2))
        def f(a,b):
            if  b<0:
                return 1
            if a<0:
                return 0
            if dp[a][b]!=-1:
                return dp[a][b]
            if t1[a]==t2[b]:
                x=f(a-1,b-1)+f(a-1,b)
            else:
                x=f(a-1,b)
            dp[a][b]=x
            return x
        return f(len(t1)-1,len(t2)-1)