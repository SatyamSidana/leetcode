class Solution:
    def islandPerimeter(self, g: List[List[int]]) -> int:
        p=0
        if len(g)==1 and len(g[0])==1:
            if g[0][0]==1:
                return 4
        if len(g)==1:
            for i in range (len(g[0])):
                if g[0][i]==1:
                    c=4
                    if i==0:
                        if g[0][i+1]==1:
                            c-=1
                    elif i==len(g[0])-1:
                        if g[0][i-1]==1:
                            c-=1
                    else:
                        if g[0][i-1]==1:
                            c-=1
                        if g[0][i+1]==1:
                            c-=1
                    p+=c
            return p
        if len(g[0])==1:
            for i in range (len(g)):
                if g[i][0]==1:
                    c=4
                    if i==0:
                        if g[i+1][0]==1:
                            c-=1
                    elif i==len(g)-1:
                        if g[i-1][0]==1:
                            c-=1
                    else:
                        if g[i-1][0]==1:
                            c-=1
                        if g[i+1][0]==1:
                            c-=1
                    p+=c
            return p
        for i in range (len(g)):
            for j in range (len(g[i])):
                if g[i][j]==1:
                    c=4
                    if i==0:
                        if j==0:
                            if g[i+1][j]==1:
                                c-=1
                            if g[i][j+1]==1:
                                c-=1
                        elif j==len(g[i])-1:
                            if g[i+1][j]==1:
                                c-=1
                            if g[i][j-1]==1:
                                c-=1
                        else:
                            if g[i+1][j]==1:
                                c-=1
                            if g[i][j+1]==1:
                                c-=1
                            if g[i][j-1]==1:
                                c-=1
                    elif i==len(g)-1:
                        if j==0:
                            if g[i-1][j]==1:
                                c-=1
                            if g[i][j+1]==1:
                                c-=1
                        elif j==len(g[i])-1:
                            if g[i-1][j]==1:
                                c-=1
                            if g[i][j-1]==1:
                                c-=1
                        else:
                            if g[i-1][j]==1:
                                c-=1
                            if g[i][j-1]==1:
                                c-=1
                            if g[i][j+1]==1:
                                c-=1
                    else:
                        if j==0:
                            if g[i-1][j]==1:
                                c-=1
                            if g[i+1][j]==1:
                                c-=1
                            if g[i][j+1]==1:
                                c-=1
                        elif j==len(g[i])-1:
                            if g[i-1][j]==1:
                                c-=1
                            if g[i+1][j]==1:
                                c-=1
                            if g[i][j-1]==1:
                                c-=1
                        else:
                            if g[i-1][j]==1:
                                c-=1
                            if g[i][j-1]==1:
                                c-=1
                            if g[i][j+1]==1:
                                c-=1
                            if g[i+1][j]==1:
                                c-=1
                    p+=c
        return p    


                

        