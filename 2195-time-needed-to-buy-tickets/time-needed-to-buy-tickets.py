class Solution:
    def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        a=len(t)
        c=0
        while t[k]!=0:
            for i in range (len(t)):
                t[i]-=1
                if i==k and t[k]==0:
                    for i in range (k):
                        if t[i]>=0:
                            c+=1
                    return c+1
            c+=a
            for i in t:
                if i==0:
                    a-=1
        return c
        