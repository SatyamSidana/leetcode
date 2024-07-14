class Solution:
    def minDistance(self, t1: str, t2: str) -> int:
        dp=[]
        for i in range (len(t1)):
            dp.append([-1]*len(t2))
        def f(a,b):
            if a<0 or b<0:
                return 0
            if dp[a][b]!=-1:
                return dp[a][b]
            if t1[a]==t2[b]:
                x=1+f(a-1,b-1)
                y=-1
            else:
                x=0+f(a-1,b)
                y=0+f(a,b-1)
            dp[a][b]=max(x,y)
            return dp[a][b]
        return len(t1)+len(t2)-2*f(len(t1)-1,len(t2)-1)