class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        m=0
        if y>x:
            i=0
            while i<len(s)-1:
                if s[i]+s[i+1]=="ba":
                    s=s[:i]+s[i+2:]
                    m+=y
                    if i>0:
                        i-=1
                else:
                    i+=1
            j=0
            while j<len(s)-1:
                if s[j]+s[j+1]=="ab":
                    s=s[:j]+s[j+2:]
                    m+=x
                    if j>0:
                        j-=1
                else:
                    j+=1
        else:
            i=0
            while i<len(s)-1:
                if s[i]+s[i+1]=="ab":
                    s=s[:i]+s[i+2:]
                    m+=x
                    if i>0:
                        i-=1
                else:
                    i+=1
            j=0
            while j<len(s)-1:
                if s[j]+s[j+1]=="ba":
                    s=s[:j]+s[j+2:]
                    m+=y
                    if j>0:
                        j-=1
                else:
                    j+=1
        return m



        