class Solution:
    def searchMatrix(self, ma: List[List[int]], t: int) -> bool:
        l=0
        m=len(ma)
        n=len(ma[0])
        h=m*n-1
        if m*n==1:
            if ma[0][0]==t:
                return True
            else:
                return False
        else:
            while(l<=h):
                mid=(l+h)//2
                a=ma[mid//n][mid%n]
                if a>t:
                    h=mid-1
                elif a<t:
                    l=mid+1
                else:
                    return True
            return False
            

        