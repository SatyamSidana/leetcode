class Solution:
    def largestOddNumber(self, n: str) -> str:
        m=-1
        b=["1","3","5","7","9"]
        for i in range (len(n)):
            if n[i] in b:
                m=i
        if m==-1:
            return ""
        return n[:m+1]
        