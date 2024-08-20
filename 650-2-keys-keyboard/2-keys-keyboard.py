class Solution:
    def minSteps(self, n: int) -> int:
        def f(i,j,k):
            if (i==n):
                return 0
            if i>n:
                return 1e9
            if k==0:
                x=min(1+f(i+j,j,1),1+f(i+j,j,0))
            else:
                x=1+f(i,i,0)
            return x
        return f(1,0,1)