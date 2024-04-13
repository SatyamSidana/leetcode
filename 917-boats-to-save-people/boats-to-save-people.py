class Solution:
    def numRescueBoats(self, p: List[int], l: int) -> int:
        p.sort()
        b=0
        c=0
        r=0
        i=0
        j=0
        
        j=len(p)-1
        while i<=j:
            while i<=j and c+p[j]<=l and r<2:
                c+=p[j]
                r+=1
                j-=1
            while i<=j and c+p[i]<=l and r<2:
                c+=p[i]
                r+=1
                i+=1
            b+=1
            c=0
            r=0
            print(i,j)
        if c:
            b+=1
        return b