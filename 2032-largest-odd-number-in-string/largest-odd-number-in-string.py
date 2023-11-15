class Solution:
    def largestOddNumber(self, n: str) -> str:
        m=""
        a=""
        b=["1","3","5","7","9"]
        for i in range (len(n)):
            a+=n[i]
            if n[i] in b:
                m=a
        return m
        