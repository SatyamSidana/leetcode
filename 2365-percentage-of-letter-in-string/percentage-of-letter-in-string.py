class Solution:
    def percentageLetter(self, s: str, l: str) -> int:
        a={}
        for i in s:
            if a.get(i):
                a[i]+=1
            else:
                a[i]=1
        if a.get(l):
            return math.floor((a[l]/len(s))*100)
        else:
            return 0
        