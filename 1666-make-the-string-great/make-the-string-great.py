class Solution:
    def makeGood(self, s: str) -> str:
        i=0
        while i <len(s)-1:
            if s[i]==chr(ord(s[i+1])-32) or s[i]==chr(ord(s[i+1])+32):
                s=s[:i]+s[i+2:]
                if i>0:
                    i-=1
            else:
                i+=1
        return s
        