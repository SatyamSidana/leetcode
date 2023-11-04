class Solution:
    def partitionString(self, s: str) -> int:
        i=0
        c=0
        a=[]
        while(i<len(s)):
            if s[i] in a:
                a=[]
                c+=1
            else:
                a.append(s[i])
                i+=1
        return c+1