class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        b=""
        for i in range (len(a)-1):
            b+=a[i][::-1]
            b+=" "
        b+=a[-1][::-1] 
        return b


        