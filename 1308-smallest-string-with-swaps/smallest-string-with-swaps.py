class Solution:
    def smallestStringWithSwaps(self, s: str, pa: List[List[int]]) -> str:
        p=[0]*(len(s))
        r=[0]*(len(s))
        for i in range (len(p)):
            p[i]=i
        def find(x):
            if p[x]==x:
                return x
            return find(p[x])
        def union(x,y):
            p1,p2=find(x),find(y)
            if p1!=p2:
                if r[p1]>r[p2]:
                    p[p2]=p1
                elif r[p1]<r[p2]:
                    p[p1]=p2
                else:
                    p[p1]=p2
                    r[p2]+=1
        for i in pa:
            union(i[0],i[1])
        a={}
        for i in range (len(p)):
            if a.get(find(i)):
                a[find(i)].append(s[i])
            else:
                a[find(i)]=[]
                a[find(i)].append(s[i])
        for i in a:
            a[i].sort()
        s=""
        for i in range (len(p)):
            s+=a[find(i)][0]
            a[find(i)].pop(0)
        return s


        