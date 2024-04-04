class Solution:
    def maxProfit(self, a: List[int]) -> int:
        s=0
        y=0
        l=0
        r=1
        while(r<len(a)):
            if(a[r]>a[l]):
                s=a[r]-a[l]
                y=max(y,s)
            else:
                l=r
            r+=1
        return y