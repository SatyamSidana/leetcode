class Solution:
    def minimumLength(self, s: str) -> int:
        a=list(s)
        if len(s)==1:
            return 1
        i=0
        j=len(s)-1
        print(len(s))
        while i<j and s[i]==s[j]:
            a=s[i]
            while i<=j and s[i]==a  :
                i+=1
            while i<j and s[j]==a :
                j-=1  
        return j-i+1

        