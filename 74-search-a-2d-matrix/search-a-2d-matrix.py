class Solution:
    def searchMatrix(self, s: List[List[int]], t: int) -> bool:
        l=0
        m=len(s)
        n=len(s[0])
        h=m-1
        while(l<=h):
            mid=(l+h)//2
            if s[mid][0]<=t<=s[mid][n-1]:
                p=s[mid]
                la=0
                hi=n-1
                while(la<=hi):
                    mi=(la+hi)//2
                    if p[mi]<t:
                        la=mi+1
                    elif p[mi]>t:
                        hi=mi-1
                    else:
                        return True
                return False
            elif s[mid][0]>t:
                h=mid-1
            else:
                l=mid+1
        return False
                    


        
            

        