class Solution:
    def sortedSquares(self, n: List[int]) -> List[int]:
    
        i=0
        j=len(n)-1
        a=[0]*len(n)
        z=len(a)-1
        while i<=j:
            if n[i]*n[i]>n[j]*n[j]:
                a[z]=n[i]*n[i]
                i+=1
            else:
                a[z]=n[j]*n[j]
                j-=1
            z-=1
        return a
                
        