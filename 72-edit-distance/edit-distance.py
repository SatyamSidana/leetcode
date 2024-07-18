class Solution:
    def minDistance(self, t1: str, t2: str) -> int:
        dp=[]
        if t2=="":
            return len(t1)
        if t1=="":
            return len(t2)
        for i in range (len(t1)):
            dp.append([-1]*len(t2))
        def f(i,j):
            if j<0:
                return int(i)+1
            if i<0:
                return j+1
            if dp[i][j]!=-1:
                return dp[i][j]
            if t1[i]==t2[j]:
                x=0+f(i-1,j-1)
            else:
                x=min(1+f(i-1,j),1+f(i,j-1),1+f(i-1,j-1))
            dp[i][j]=x
            return x
        return f(len(t1)-1,len(t2)-1)