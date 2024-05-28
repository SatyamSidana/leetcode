class Solution:
    def countServers(self, g: List[List[int]]) -> int:
        c={}
        r={}
        count=0
        
        for i in range (len(g)):
            for j in range (len(g[i])):
                if g[i][j]==1:
                    if c.get(j):
                        c[j]+=1
                    else:
                        c[j]=1
                    if r.get(i):
                        r[i]+=1
                    else:
                        r[i]=1
        for i in range (len(g)):
            for j in range (len(g[i])):
                if g[i][j]==1:
                    if c.get(j)>1 or r.get(i)>1:
                        count+=1
        return count