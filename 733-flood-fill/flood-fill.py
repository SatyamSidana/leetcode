class Solution:
    def floodFill(self, m: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        i=sr
        j=sc
        q=[]
        q.append([i,j])
        c=m[i][j]
        if c==color:
            return m
        m[i][j]=color
        while q:
            b=q.pop(0)
            if b[0]!=0 and m[b[0]-1][b[1]]==c:
                m[b[0]-1][b[1]]=color
                q.append([b[0]-1,b[1]])
            if b[1]!=0 and m[b[0]][b[1]-1]==c:
                m[b[0]][b[1]-1]=color
                q.append([b[0],b[1]-1])
            if b[0]!=len(m)-1 and m[b[0]+1][b[1]]==c:
                m[b[0]+1][b[1]]=color
                q.append([b[0]+1,b[1]])
            if b[1]!=len(m[0])-1 and m[b[0]][b[1]+1]==c:
                m[b[0]][b[1]+1]=color
                q.append([b[0],b[1]+1])
        return m
            


            