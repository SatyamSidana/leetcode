class Solution:
    def minCost(self, c: str, t: List[int]) -> int:
        m=0
        i=0
        while(i<len(c)-1):
            if c[i]==c[i+1]:
                d=c[i]
                b=[]
                while i<len(c):
                    if c[i]==d:
                        b.append(t[i])
                        i+=1
                    else:
                        break
                m+=sum(b)-max(b)
            else:
                i+=1
        return m            



        