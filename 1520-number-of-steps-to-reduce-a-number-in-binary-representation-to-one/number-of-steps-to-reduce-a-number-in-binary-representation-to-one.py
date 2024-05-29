class Solution:
    def numSteps(self, s: str) -> int:
        n=0
        c=0
        s=s[::-1]
        for i in range (len(s)):
            if s[i]=="1":
                n+=2**i
        while n>1:
            if n%2==0:
                n=n//2
            else:
                n+=1
            c+=1
        return c