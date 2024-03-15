class Solution:
    def numIslands(self, g: List[List[str]]) -> int:
        t=False
        v=[[0]*len(g[0])]*len(g)
        q=[]
        c=0
        for i in range (len(g)):
            for j in range (len(g[0])):
                while q:
                    b=q.pop(0)
                    if b[0]!=0 and g[b[0]-1][b[1]]=="1":
                        g[b[0]-1][b[1]]=0
                        q.append((b[0]-1,b[1]))
                    if b[0]!=len(g)-1 and g[b[0]+1][b[1]]=="1":
                        g[b[0]+1][b[1]]=0
                        q.append((b[0]+1,b[1]))
                    if b[1]!=0 and g[b[0]][b[1]-1]=="1":
                        g[b[0]][b[1]-1]=0
                        q.append((b[0],b[1]-1))
                    if b[1]!=len(g[0])-1 and g[b[0]][b[1]+1]=="1":
                        g[b[0]][b[1]+1]=0
                        q.append((b[0],b[1]+1))
                    t=True
                if t==True:
                    c+=1
                if g[i][j]=="1":
                    q.append((i,j))
                t=False
        if q:
            c+=1
        return c