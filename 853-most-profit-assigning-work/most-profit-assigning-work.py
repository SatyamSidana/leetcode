class Solution:
    def maxProfitAssignment(self, d: List[int], p: List[int], w: List[int]) -> int:
        m=0
        c=0
        a=[]
        for i in range (len(d)):
            a.append([d[i],p[i]])
        a.sort()
        w.sort()
        j=0
        for i in w:
            while j<len(a) and i>=a[j][0] :
                c=max(c,a[j][1])
                j+=1
            m+=c
        return m

        