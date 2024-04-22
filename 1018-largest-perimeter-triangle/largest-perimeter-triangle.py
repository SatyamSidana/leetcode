class Solution:
    def largestPerimeter(self, n: List[int]) -> int:
        n.sort()
        c=0
        for i in range (2,len(n)):
            h=i-1
            l=i-2
            if n[h]+n[l]>n[i]:
                c=max(c,n[h]+n[l]+n[i])
        return c
                

        
        