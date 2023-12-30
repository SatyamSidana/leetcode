class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        a={}
        for i in m:
            if a.get(i):
                a[i]+=1
            else:
                a[i]=1
        for i in r:
            if a.get(i) and a[i]!=0:
                a[i]-=1
            else:
                return False
        return True
