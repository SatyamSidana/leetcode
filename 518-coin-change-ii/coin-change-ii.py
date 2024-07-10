class Solution:
    def change(self, s: int, c: List[int]) -> int:
        dp=[]
        for i in range(len(c)):
            dp.append([-1]*(s+1))
        def f(i,t):
            if i==len(c)-1:
                if t%c[i]==0:
                    return 1
                else:
                    return 0
            if dp[i][t]!=-1:
                return dp[i][t]
            a=f(i+1,t)
            b=0
            if t>=c[i]:
                b=f(i,t-c[i])
            dp[i][t]=a+b
            return a+b
        x=f(0,s)
        if x==1e9:
            return -1
        return x