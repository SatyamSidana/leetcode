class Solution:
    def cherryPickup(self, g: List[List[int]]) -> int:
        dp=[]
        for i in range (71):
            dp.append([])
            for j in range (71):
                dp[i].append([-1]*71)
        def calc(x,y,z):
            if dp[x][y][z]!=-1:
                return dp[x][y][z]
            k=0
            if y!=z:
                k=g[x][y]+g[x][z]
            else:
                k=g[x][y]
            if x==len(g)-1 :
                return k
            ma=0
            for i in ([-1,0,1]):
                for j in ([-1,0,1]):
                    if 0<=i+y<=len(g[0])-1 and 0<=j+z<=len(g[0])-1:
                        ma=max(ma,calc(x+1,y+i,z+j))
            dp[x][y][z]=ma+k
            return dp[x][y][z]
        a=calc(0,0,len(g[0])-1)
        print(a)
        return a
                    
            