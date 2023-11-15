class Solution:
    def successfulPairs(self, sp: List[int], p: List[int], s: int) -> List[int]:
        p.sort()
        b=len(p)
        a=[0]*len(sp)
        for i in range (len(sp)):
            l=0
            h=b-1
            t=s/sp[i]
            print(t)
            while(l<=h):
                mid=(l+h)//2
                if p[mid]<t:
                    l=mid+1
                elif p[mid]>t:
                    h=mid-1
                else:
                    lh=l
                    h=mid-1
            a[i]=b-l
        return a

        