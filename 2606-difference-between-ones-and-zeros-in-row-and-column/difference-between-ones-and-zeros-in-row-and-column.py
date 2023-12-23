class Solution:
    def onesMinusZeros(self, g: List[List[int]]) -> List[List[int]]:
        a=[0]*len(g)
        b=[0]*len(g)
        c=[0]*len(g[0])
        d=[0]*len(g[0])
        for i in range (len(g)):
            for j in range (len(g[0])):
                if g[i][j]==1:
                    a[i]+=1
                    c[j]+=1
                else:
                    b[i]+=1
                    d[j]+=1
        print(a)
        print(b)
        print(c)
        print(d)
        x=[]
        for i in range (len(a)):
            y=[]
            for j in range (len(c)):
                z=a[i]-b[i]+c[j]-d[j]
                y.append(z)
            x.append(y)
        return x





