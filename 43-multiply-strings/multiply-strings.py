class Solution:
    def multiply(self, n1: str, n2: str) -> str:
        if n1[0]=='0' or n2[0]=='0':
            return '0'
        a,b=0,0
        for i,j in enumerate(n1):
            a+=(ord(j)-ord('0'))*(10**(len(n1)-i-1))
        for i,j in enumerate(n2):
            b+=(ord(j)-ord('0'))*(10**(len(n2)-i-1))
        c=a*b
        ans=""
        while c>0:
            ans+=chr(ord('0')+(c%10))
            c//=10
        return ans[::-1]
        
