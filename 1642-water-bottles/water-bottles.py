class Solution:
    def numWaterBottles(self, n: int, e: int) -> int:
        a=0
        r=0
        j=-1
        while j!=0:
            a+=n
            j=(n+r)//e
            r=(n+r)%e
            n=j
            
        return a
