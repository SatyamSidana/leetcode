class Solution:
    def duplicateZeros(self, a: List[int]) -> None:
        i=0
        while i<len(a):
            if a[i]==0:
                a.insert(i+1,0)
                a.pop()
                i+=2
            else:
                i+=1
        
        