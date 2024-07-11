class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp=[]
        for i in range(len(s)):
            dp.append([-1]*len(s))
        def f(a,b):
            if a==b:
                return 1
            if a>b:
                return 0
            if dp[a][b]!=-1:
                return dp[a][b]
            if s[a]==s[b]:
                x=2+f(a+1,b-1)
                y=0
            else:
                x=0+f(a+1,b)
                y=0+f(a,b-1)
            dp[a][b]=max(x,y)
            return max(x,y)
        return f(0,len(s)-1)