class Solution:
    def countSubarrays(self, n: List[int], k: int) -> int:
        a=0
        s=0
        e=0
        m=max(n)
        c=0
        while e<len(n):
            if n[e]==m:
                a+=1
            while a>=k:
                if n[s]==m:
                    a-=1
                c+=len(n)-e
                s+=1
            e+=1      
        return c