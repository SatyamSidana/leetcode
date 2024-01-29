class Solution:
    def findDuplicate(self, n: List[int]) -> int:
        a=[0]*len(n)
        for i in range (len(n)):
            if a[n[i]-1]!=0:
                return n[i]
            else:
                a[n[i]-1]=n[i]
               