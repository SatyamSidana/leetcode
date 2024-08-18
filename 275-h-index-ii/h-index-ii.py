class Solution:
    def hIndex(self, c: List[int]) -> int:
        def valid(n):
            l=0
            h=len(c)-1
            res=-1
            while(l<=h):
                mid=(l+h)//2
                if(c[mid]>=n):
                    res=len(c)-mid
                    h=mid-1
                else:
                    l=mid+1
            if n<=res:
                return True
            else:
                return False
        l=0
        h=1000
        ans=0
        while(l<=h):
            mid=(l+h)//2
            if valid(mid):
                ans=mid
                l=mid+1
            else:
                h=mid-1
        return ans
        