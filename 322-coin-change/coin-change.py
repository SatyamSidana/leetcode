class Solution:
    def coinChange(self, c: List[int], s: int) -> int:
        dp=[]
        for i in range(len(c)):
            dp.append([-1]*(s+1))
        def f(i,t):
            if i==len(c)-1:
                if t%c[i]==0:
                    return t//c[i]
                else:
                    return 1e9
            if dp[i][t]!=-1:
                return dp[i][t]
            a=0+f(i+1,t)
            b=1e9
            if t>=c[i]:
                b=1+f(i,t-c[i])
            dp[i][t]=min(a,b)
            return min(a,b)
        x=f(0,s)
        if x==1e9:
            return -1
        return x
            