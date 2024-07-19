class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[]
        for i in range (len(s)):
            dp.append([-1]*len(p))
        def f(i,j):
            if i<0 and p[:j+1]=="*"*(j+1):
                return True
            if j==0 and i==0:
                if s[i]==p[j] or p[j]=="?" or p[j]=="*":
                    return True
                else:
                    return False
            if i<0  or j<0:
                return False
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==p[j] or p[j]=="?":
                x=f(i-1,j-1)
            elif p[j]=="*":
                x=f(i-1,j-1)|f(i-1,j)|f(i,j-1)
            else:
                return False
            dp[i][j]=x
            return x
        return f(len(s)-1,len(p)-1)
            