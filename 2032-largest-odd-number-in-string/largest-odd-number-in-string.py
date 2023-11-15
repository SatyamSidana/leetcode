class Solution:
    def largestOddNumber(self, n: str) -> str:
        m=""
        a=""
        b=["1","3","5","7","9"]
        for i in n:
            a+=i
            if i in b:
                m=a
        return m
        