class Solution:
    def canPartition(self, n: List[int]) -> bool:
        s=sum(n)//2
        if sum(n)%2==1:
            return False
        dp=[]
        for i in range (len(n)):
            dp.append([-1]*(s+1))
        def f(i,t):
            if t==0:
                return True
            if i==len(n)-1:
                return False
            if dp[i][t]!=-1:
                return dp[i][t]
            a=False
            if t>=n[i]:
                t-=n[i]
                i+=1
                a=f(i,t)
                i-=1
                t+=n[i]
            i+=1
            b=f(i,t)
            dp[i][t]=a|b
            return dp[i][t]
        return f(0,s)

        