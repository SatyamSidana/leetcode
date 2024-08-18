class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans=0
        c=0
        x=0
        for i in range (len(s)):
            if(s[i]=='0'):
                c+=1
            else:
                x+=1
            y0=c
            y1=x
            if y0<=k or y1<=k:
                    ans+=1
            for j in range (i):
                if(s[j]=="0"):
                    y0-=1
                else:
                    y1-=1
                if y0<=k or y1<=k:
                    ans+=1
        return ans
