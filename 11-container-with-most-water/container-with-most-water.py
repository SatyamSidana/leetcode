class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        ma=0
        while(l<=r):
            ma=max(ma,min(h[r],h[l])*(r-l))
            if h[r]>h[l]:
                l+=1
            else:
                r-=1
        return ma
            
        