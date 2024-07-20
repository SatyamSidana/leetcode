class Solution:
    def maxProfit(self, p: List[int]) -> int:
        dp={}

        def f(i,j,c):
            if c==4:
                return 0
            if i>len(p)-1:
                return 0
            if (i,j,c) in dp:
                return dp[(i,j,c)]
            if j==1:
                x=max(-p[i]+f(i+1,0,c+1),f(i+1,1,c))
            else:
                x=max(p[i]+f(i+1,1,c+1),f(i+1,0,c))
            dp[(i,j,c)]=x
            return x
        f(0,1,0)
        return f(0,1,0)
            

            