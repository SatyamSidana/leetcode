class Solution:
    def sortedSquares(self, n: List[int]) -> List[int]:
        if n[0]>=0:
            a=[]
            for i in n:
                a.append(i*i)
        elif n[len(n)-1]<0:
            a=[]
            i=len(n)-1
            while i>=0:
                a.append(n[i]*n[i])
                i-=1
        else:
            i=0
            j=len(n)-1
            a=[0]*len(n)
            z=len(a)-1
            while i<=j:
                if n[i]*n[i]>n[j]*n[j]:
                    a[z]=n[i]*n[i]
                    i+=1
                else:
                    a[z]=n[j]*n[j]
                    j-=1
                z-=1
        return a
                
        