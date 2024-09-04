class Solution:
    def divide(self, di: int, dr: int) -> int:
        n=False
        d=False
        if di>0:
            n=True
        if dr>0:
            d=True
        if n==d:
            ans=di//dr
        else:
            ans=ceil(di/dr)
        if ans<-(2**31):
            return -2**31
        elif ans>(2**31)-1:
            return (2**31)-1
        else:
            return ans

        