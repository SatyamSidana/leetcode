class Solution:
    def maxScore(self, s: str) -> int:
        l=0
        r=0
        m=0
        for i in s:
            if i =="1":
                r+=1
        print(r)
        for i in range (len(s)-1):
            print(l,r)
            if s[i]=="1":
                r=r-1
                m=max(m,l+r)
            else:
                l=l+1
                m=max(m,l+r)
        return m


        