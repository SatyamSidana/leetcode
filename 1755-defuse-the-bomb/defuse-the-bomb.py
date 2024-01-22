class Solution:
    def decrypt(self, c: List[int], k: int) -> List[int]:
        n=len(c)
        a=[]
        if k==0:
            return [0]*n
        elif k>0:
            b=c+c[:k]
            m=sum(c[:k])
            for i in range (n):
                m=m-b[i]+b[i+k]
                a.append(m)
        elif k<0:
            b=c[n+k:]+c
            m=sum(c[n+k:])
            a.append(m)
            i=-k+1
            while i<len(b):
                m=m+b[i-1]-b[i+k-1]
                a.append(m)
                i+=1
        return a


        