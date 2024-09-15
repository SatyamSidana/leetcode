class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        dp=[-1]*len(arr)
        v=[False]*n
        def f(i):
            if i>=n or i<0:
                return False
            if arr[i]==0:
                return True
            if v[i]:
                return False
            v[i]=True
            if dp[i]!=-1:
                return dp[i]
            x= f(i+arr[i] )or f(i-arr[i])
            dp[i]=x
            return x
        return f(start)