class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, a: List[int]) -> int:
        a.sort()
        a[0]=1
        for i in range (len(a)-1):
            if abs(a[i]-a[i+1])>1 :
                a[i+1]=a[i]+1
        return max(a)
            
        