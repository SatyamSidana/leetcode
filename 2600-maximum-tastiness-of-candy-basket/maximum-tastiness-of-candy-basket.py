class Solution:
    def maximumTastiness(self, p: List[int], k: int) -> int:
        p.sort()
        def isvalid(num):
            c=1
            diff=num+p[0]
            for i in range (1,len(p)):
                if p[i]>=diff:
                    c+=1
                    diff=num+p[i]
            return c
        l=0
        h=p[-1]-p[0]
        ans=0
        while l<=h:
            mid=(l+h)//2
            if isvalid(mid)>=k:
                ans=mid
                l=mid+1
            else:
                h=mid-1
        return ans
        