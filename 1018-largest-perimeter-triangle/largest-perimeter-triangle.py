class Solution:
    def largestPerimeter(self, n: List[int]) -> int:
        n.sort()
        c=0
        for i in range (2,len(n)):
            j=len(n)-i+1
            h=j-1
            l=j-2
            if n[h]+n[l]>n[j]:
                c=max(c,n[h]+n[l]+n[j])
                break
        return c
                

        
        