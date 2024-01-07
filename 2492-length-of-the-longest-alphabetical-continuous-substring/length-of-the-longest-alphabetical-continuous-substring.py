class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        r=0
        m=1
        while(r<len(s)-1):
            if s[r]==chr(ord(s[r+1])-1):
                c=2
                r+=1
                if r<len(s)-1:
                    while s[r]==chr(ord(s[r+1])-1):
                        r+=1
                        c+=1
                        if r>len(s)-2:
                            break
                    m=max(m,c)
            else:
                r+=1
        return m 

        