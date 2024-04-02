class Solution:
    def maximum69Number (self, n: int) -> int:
        m=list(str(n))
        for i in range (len(m)):
            if m[i]=="6":
                m[i]="9"
                break
        return int("".join(m))
        