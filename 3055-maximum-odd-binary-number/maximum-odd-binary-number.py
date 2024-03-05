class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c=0
        for i in s:
            if i=="1":
                c+=1
        a="1"
        b="0"
        return a*(c-1)+b*(len(s)-c)+a
        