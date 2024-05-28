class Solution:
    def equalSubstring(self, s: str, t: str, mc: int) -> int:
        m=0
        st=0
        e=0
        ma=0
        while e<len(s):
            while mc>=m and e<len(s):
                m+=abs(ord(s[e])-ord(t[e]))
                e+=1
            if e>=len(s) and mc>=m:
                return max(ma,e-st)
            ma=max(ma,e-st-1)
            print(e,st)
            while mc<m and st<e:
                m-=abs(ord(s[st])-ord(t[st]))
                st+=1
            
        return ma
            