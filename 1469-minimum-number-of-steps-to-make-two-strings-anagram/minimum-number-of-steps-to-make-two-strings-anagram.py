class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a={}
        m=0
        for i in s:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in t:
            if a.get(i) and a[i]>0:
                a[i]-=1
        for i in a:
            m+=a[i]
        return m
            
        