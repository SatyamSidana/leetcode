class Solution:
    def zeroFilledSubarray(self, n: List[int]) -> int:
        i=0
        m=0
        while i < len(n):
            if n[i]==0:
                c=1
                i+=1
                while i<len(n):
                    if n[i]==0:
                        c+=1
                        i+=1
                    else:
                        break
                for j in range (c):
                    m+=j+1
            else:
                i+=1
        return m



        