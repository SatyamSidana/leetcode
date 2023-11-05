class Solution:
    def getAverages(self, n: List[int], k: int) -> List[int]:
        a=[-1]*len(n)
        b=0
        if len(n)>2*k:
            for i in range (2*k+1):
                b+=n[i]
            for i in range (len(n)-2*k-1):
                a[k+i]=b//(2*k+1)
                b=b-n[i]+n[2*k+1+i]
            a[len(n)-k-1]=b//(2*k+1)
            return a
        else:
            return a
        