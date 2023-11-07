class Solution:
    def eliminateMaximum(self, d: List[int], s: List[int]) -> int:
        c=0
        t=[]
        for i in range (0,len(d)):
            t.append(d[i]/s[i])
        t.sort()
        for i in range (len(t)):
            if t[i]>i:
                c+=1
            else:
                break
        return c

         
        