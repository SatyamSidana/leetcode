class Solution:
    def largestSumAfterKNegations(self, n: List[int], k: int) -> int:
        n.sort()
        m=0
        i=0
        while i<len(n) and n[i]<0 and k>0:
            n[i]*=-1
            k-=1
            i+=1
        if i<len(n):
            if k%2==0:
                pass
            else:
                if i!=0 and n[i]>=n[i-1]:
                    n[i-1]*=-1
                else:
                    n[i]*=-1
        else:
           if k%2!=0:
            n[-1]*=-1 
        return sum(n)

        