class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        p=[]
        b=""
        for i in range (26):
            p.append(i)
        def find(x):
            if x==p[x]:
                return x
            return find(p[x])
        def union(x,y):
            xr=find(x)
            yr=find(y)
            if xr>yr:
                p[xr]=yr
            else:
                p[yr]=xr
            print(x,p[x],y,p[y])
        for i in range (len(s1)):
            union(ord(s1[i])-ord("a"),ord(s2[i])-ord("a"))
        
        print(p)
        for i in  baseStr:
            b+=chr(ord("a")+find(ord(i)-ord("a")))
        return b

        