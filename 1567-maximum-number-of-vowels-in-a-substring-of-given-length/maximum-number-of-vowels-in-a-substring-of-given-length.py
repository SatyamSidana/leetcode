class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0
        r=k
        m=0
        a=["a","e","i","o","u"]
        for i in range (k):
            if s[i] in a:
                m+=1
        b=m
        while r<len(s):
            if s[l] in a:
                b-=1
            if s[r] in a:
                b+=1
            m=max(m,b)
            l+=1
            r+=1
        return m

            
        