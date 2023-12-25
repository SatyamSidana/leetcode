class Solution:
    def buyChoco(self, p: List[int], m: int) -> int:
        p.sort()
        minn=m+1
        for i in range (len(p)-1):
            if m-p[i]-p[i+1]>=0:
                minn=min(minn,p[i]+p[i+1])
            else:
                if minn>m:
                    return minn-1
                else :
                    return m-minn
        return m-minn
        