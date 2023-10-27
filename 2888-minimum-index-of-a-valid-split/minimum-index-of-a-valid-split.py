class Solution:
    def minimumIndex(self, n: List[int]) -> int:
        a={}
        b=len(n)
        s=0
        for i in range (b):
            if n[i] in a:
                a[n[i]]=a.get(n[i])+1
            else:
                a[n[i]]=1
            if a.get(n[i])*2>len(n)+1:
                s=n[i]
        l,r=0,a.get(s)
        for i in range (b):
            if n[i]==s:
                l+=1
                r-=1
            if l*2>i+1 and r*2>b-i-1:
                return i    
        
        return -1


