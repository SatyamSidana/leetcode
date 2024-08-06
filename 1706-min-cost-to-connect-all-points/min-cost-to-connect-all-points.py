class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        def find(x):
            if x==pa[x]:
                return x
            else:
                return find(pa[x])
        def union(x,y):
            xi=find(x)
            yi=find(y)
            if r[xi]>r[yi]:
                pa[yi]=xi
            if r[yi]>r[xi]:
                pa[xi]=yi
            else:
                r[xi]+=1
                pa[yi]=xi
        pa=[0]*len(p)
        r=[0]*len(p)
        for i in range (len(pa)):
            pa[i]=i
        a={}
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                a[(i,j)]=abs(p[i][0]-p[j][0])+abs(p[i][1]-p[j][1])
        a=sorted(a.items(),key=lambda x:x[1])
        ans=0
        m=1
        for i in a:
            if find(i[0][0])==find(i[0][1]):
                pass
            else:
                union(i[0][0],i[0][1])
                ans+=i[1]
                m+=1
                if m==len(p):
                    break
        return ans