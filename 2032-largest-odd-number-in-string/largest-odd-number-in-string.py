class Solution:
    def largestOddNumber(self, n: str) -> str:
        m=-1
        b={"1":1,"3":1,"5":1,"7":1,"9":1}
        i=len(n)-1
        while(i>=0):
            if b.get(n[i]):
                m=i
                break
            i-=1
        if m==-1:
            return ""
        return n[:m+1]
        