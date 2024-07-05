class Solution:
    m=10^9
    def minimumTotal(self, t: List[List[int]]) -> int:
        
        dp=[]
        for i in range (len(t)):
            dp.append([-1]*(i+1))
        dp.append([(-1)]*(len(t)+1))
        def calc(x,y):
            if x==len(t)-1:
                dp[x][y]=t[x][y]
                return t[x][y]
            if dp[x+1][y+1]!=-1:
                a=dp[x+1][y+1]
            else:
                a=calc(x+1,y+1)
            if dp[x+1][y]!=-1:
                b=dp[x+1][y]
            else:
                b=calc(x+1,y)
            dp[x][y]=min(a,b)+t[x][y]
            return (min(a,b)+t[x][y])
        calc(0,0)
        return dp[0][0]
            