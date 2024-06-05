class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[]
        for i in range (n+1):
            c=0
            while i>0:
                i=i&(i-1)
                c+=1
            a.append(c)
        return a