class Solution:
    def finalPrices(self, p: List[int]) -> List[int]:
        a=[]
        for i in range (len(p)-1):
            t=True
            for j in range (i+1,len(p)):
                if p[j]<=p[i]:
                    a.append(p[i]-p[j])
                    t=False
                    break
            if t:
                a.append(p[i])
        a.append(p[len(p)-1])
        return a