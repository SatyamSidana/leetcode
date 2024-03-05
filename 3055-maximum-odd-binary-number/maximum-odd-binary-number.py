class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c=0
        for i in s:
            if i=="1":
                c+=1
        return "1"*(c-1)+"0"*(len(s)-c)+"1"
        