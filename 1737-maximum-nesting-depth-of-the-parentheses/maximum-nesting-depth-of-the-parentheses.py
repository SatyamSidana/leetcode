class Solution:
    def maxDepth(self, s: str) -> int:
        m=0
        a=[]
        c=0
        for i in range (len(s)):
            if s[i]==")":
                c-=1
                a.append(s[i])
            elif s[i]=="(":
                c+=1
                a.append(s[i])
                m=max(m,c)
            if c==0:
                a=[]
        return m

        