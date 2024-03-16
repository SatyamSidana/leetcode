class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        c=0
        a=[0]*(n)
        for i in range (2,n):
            if a[i]==0:
                j=2
                while i*j<n:
                    a[i*j]=1
                    j+=1
        for i in a:
            if i==0:
                c+=1
        return c-2
        