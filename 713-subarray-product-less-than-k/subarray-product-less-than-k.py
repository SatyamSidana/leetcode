class Solution:
    def numSubarrayProductLessThanK(self, n: List[int], k: int) -> int:
        s=0
        e=0
        w=1
        c=0
        if k==0 or k==1:
            return 0
        while(e<len(n)):
            w*=n[e]
            a=w
            e+=1
            while (s<e) and (w>=k):
                w=w//n[s]
                s+=1
            c+=e-s
        return c


                