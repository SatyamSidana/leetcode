class Solution:
    def maximumSwap(self, num: int) -> int:
        s=list(str(num))
        a=sorted(s)
        b=a[::-1]
        c=-1
        d=-1
        for i in range (len(s)):
            if b[i]==s[i]:
                i+=1
            else:
                c=b[i]
                d=s[i]
                s[i]=c
                break
        if c==-1:
            return num
        i=len(s)-1
        while i>=0:
            if s[i]==c:
                break
            i-=1
        s[i]=d
        s="".join(s)
        return int(s)
        