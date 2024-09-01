class Solution:
    def reverse(self, x: int) -> int:
        def rev(n):
            ans=0
            p=0
            while n>0:
                ans=ans*10+n%10
                n=n//10
            return ans
        if x<0:
            a=-(rev(-x))
            if a<-2**31:
                return 0
            return a
        a=rev(x)
        if a>(2**31)-1:
            return 0
        return a