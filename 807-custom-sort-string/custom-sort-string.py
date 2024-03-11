class Solution:
    def customSortString(self, order: str, s: str) -> str:
        a={}
        r=""
        for i in s:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in order:
            if i in a:
                r+=i*a[i]
                a[i]=0
        for i in a:
            if a[i]!=0:
                r+=i*a[i]
        return r

        