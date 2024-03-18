class Solution:
    def isHappy(self, n: int) -> bool:
        def sum(a):
            c=0
            while a!=0:
                c+=(a%10)**2
                a=a//10
            return c
        i=100
        while i>0:
            if sum(n)==1:
                return True
            n=sum(n)
            i-=1 
        return False     
        