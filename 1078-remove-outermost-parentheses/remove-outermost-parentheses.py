class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        m=""
        a=[]
        a.append(s[0])
        c=1
        for i in range (1,len(s)):
            if s[i]==")":
                c-=1
            else:
                c+=1
            a.append(s[i])
            if c==0:
                a.pop()
                a.pop(0)
                m+="".join(a)
                
                a=[]
        return m



        
        