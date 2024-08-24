class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        h=num
        while l<=h:
            mid=(l+h)//2
            if mid*mid>num:
                h=mid-1
            elif mid*mid<num:
                l=mid+1
            else:
                return True
        return False