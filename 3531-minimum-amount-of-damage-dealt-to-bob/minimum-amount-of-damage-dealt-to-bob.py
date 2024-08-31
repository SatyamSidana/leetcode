
class Solution:
    def minDamage(self, p: int, d: List[int], h: List[int]) -> int:
        a=[(d[i],h[i]) for i in range (len(d))]
        ans=0
        def cmp(a,b):
            d0,h0=a[0],a[1]
            d1,h1=b[0],b[1]
            t0=ceil(h0/p)
            t1=ceil(h1/p)
            if d0*t0+d1*(t1+t0)>=d1*t1+d0*(t1+t0):
                return 1
            return -1
        a.sort(key=cmp_to_key(cmp))
        print(a)
        m=sum(d)
        for i in a:
            ans+=m*(ceil(i[1]/p))
            m-=i[0]
        return ans