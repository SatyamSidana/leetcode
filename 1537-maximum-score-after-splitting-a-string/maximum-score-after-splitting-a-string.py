class Solution:
    def maxScore(self, s: str) -> int:
        l=0
        r=s.count("1")
        m=0
        for i in range (len(s)-1):
            if s[i]=="1":
                r=r-1
                m=max(m,l+r)
            else:
                l=l+1
                m=max(m,l+r)
        return m


        