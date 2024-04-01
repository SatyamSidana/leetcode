class Solution:
    def numEnclaves(self, g: List[List[int]]) -> int:
        c=0
        m=0
        t=True
        for i in range (len(g)):
            for j in range (len(g[0])):
                if g[i][j]==1:
                    q=[]
                    q.append([i,j])
                    g[i][j]=0
                    while q:
                        b=q.pop(0)
                        m+=1
                        if b[0]!=0 and g[b[0]-1][b[1]]==1:
                            g[b[0]-1][b[1]]=0
                            q.append([b[0]-1,b[1]])
                        if b[1]!=0 and g[b[0]][b[1]-1]==1:
                            g[b[0]][b[1]-1]=0
                            q.append([b[0],b[1]-1])
                        if b[0]!=len(g)-1 and g[b[0]+1][b[1]]==1:
                            g[b[0]+1][b[1]]=0
                            q.append([b[0]+1,b[1]])
                        if b[1]!=len(g[0])-1 and g[b[0]][b[1]+1]==1:
                            g[b[0]][b[1]+1]=0
                            q.append([b[0],b[1]+1])
                        if b[0]==0 or b[1]==0 or b[0]==len(g)-1 or b[1]==len(g[0])-1:
                            t=False
                    if t:
                        c+=m
                    m=0
                    t=True
        return c                      
        