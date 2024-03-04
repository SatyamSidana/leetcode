class Solution:
    def bagOfTokensScore(self, t: List[int], p: int) -> int:
        t.sort()
        i=0
        j=len(t)-1
        s=0
        if len(t)==1 and t[0]<=p:
            return 1
        while i<j:
            while t[i]<=p:
                p-=t[i]
                s+=1
                i+=1
            if i<j and s>0:    
                p+=t[j]
                j-=1
                s-=1
            if t[i]>p and s==0:
                break
        if i==j and t[i]<=p:
            s+=1
        return s