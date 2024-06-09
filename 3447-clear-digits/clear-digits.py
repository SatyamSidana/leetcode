class Solution:
    def clearDigits(self, s: str) -> str:
        i=0
        j=0
        s=list(s)
        while i<len(s):
            if s[i].isdigit():
                if i!=0:
                    s.pop(i)
                    s.pop(i-1)
                else:
                    s.pop(i)
                if i!=0:
                    i-=1
            else:
                i+=1
        return "".join(s)
