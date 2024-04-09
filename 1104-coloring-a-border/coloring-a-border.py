class Solution:
    def colorBorder(self, g: List[List[int]], row: int, col: int, c: int) -> List[List[int]]:
        a=[]
        s=g[row][col]
        v=[]
        for i in range (len(g)):
            v.append([])
            for j in range (len(g[0])):
                v[i].append(0)
        def color(x,y):
            v[x][y]=1
            if x!=0 and g[x-1][y]==s:
                if not v[x-1][y]:
                    color(x-1,y)
            if x!=len(g)-1 and g[x+1][y]==s:
                if not v[x+1][y]:
                    color(x+1,y)
            if y!=0 and g[x][y-1]==s:
                if not v[x][y-1]:
                    color(x,y-1)
            if y!=len(g[0])-1 and g[x][y+1]==s:
                if not v[x][y+1]:
                    color(x,y+1)
            if x==0 or g[x-1][y]!=s:
                a.append([x,y])
            elif x==len(g)-1 or g[x+1][y]!=s:
                a.append([x,y])
            elif y==len(g[0])-1 or g[x][y+1]!=s:
                a.append([x,y])
            elif y==0 or g[x][y-1]!=s:
                a.append([x,y])
        color(row,col)
        for i in a:
            g[i[0]][i[1]]=c
        return g
                        
                    
