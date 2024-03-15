class Solution:
    def productExceptSelf(self, n: List[int]) -> List[int]:
        p=[]
        s=[0]*len(n)
        p.append(1)
        a=[]
        s[-1]=1
        for i in range (0,len(n)-1):
            p.append(p[i]*n[i])
        i=len(n)-2
        while i>=0:
            s[i]=n[i+1]*s[i+1]
            i-=1
        for i in range (len(n)):
            a.append(p[i]*s[i])
        return a
