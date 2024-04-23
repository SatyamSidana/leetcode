class Solution:
    def brokenCalc(self, s: int, t: int) -> int:
        c=0
        while t>s:
            if t%2==0:
                t=t//2
                c+=1
            else:
                t=(t+1)//2
                c+=2
            print(c)
        c+=s-t
        return c