class Solution:
    def largestOddNumber(self, n: str) -> str:
        m=-1
        b={"1":1,"3":1,"5":1,"7":1,"9":1}
        for i in range (len(n)):
            if b.get(n[i]):
                m=i
        if m==-1:
            return ""
        return n[:m+1]
        