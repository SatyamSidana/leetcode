class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        p=[]
        s=[0]*n
        p.append(1)
        for i in range (2,n+1):
            p.append(i+p[i-2])
        i=n-1
        s[n-1]=n
        while i>0:
            s[i-1]=i+s[i]
            i-=1
        for i in range (len(p)):
            if s[i]==p[i]:
                return i+1
        return -1


        