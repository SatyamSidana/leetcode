class Solution:
    def heightChecker(self, h: List[int]) -> int:
        a=[]
        for i in h:
            a.append(i)
        h.sort()
        print(a,h)
        c=0
        for i in range (len(h)):
            if a[i]!=h[i]:
                c+=1
        return c