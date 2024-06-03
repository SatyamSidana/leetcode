class Solution:
    def reverseBits(self, n: int) -> int:
        r=0
        a=32
        while a>0:
            r=r<<1
            
            if n&1==1:
                r=r^1 
            n=n>>1
            a-=1
        return r