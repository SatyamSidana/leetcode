class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s=list(s)
        a=[]
        c=[]
        for i in range (len(s)):
            if s[i]==")" :
                if len(a)!=0:
                    a.pop()
                else:
                    c.append(i)
            elif s[i]=="(":
                a.append(i)
        a=a+c
        a.sort()
        for i in range (len(a)):
            s.pop(a[i]-i)
        return "".join(s)            