class Solution:
    def maxSatisfied(self, co: List[int], g: List[int], m: int) -> int:
        c=0
        for i in range (len(co)):
            if g[i]==0:
                c+=co[i]
        s=0
        e=0
        ma=0
        n=0
        while e<len(co):
            if g[e]==1:
                n+=co[e] 
            if e-s+1>m:
                if g[s]==1:
                    n-=co[s]
                s+=1
                
            ma=max(ma,n)
            e+=1
        return c+ma
            

