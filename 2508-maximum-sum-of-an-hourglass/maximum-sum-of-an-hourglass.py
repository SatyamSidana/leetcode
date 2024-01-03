class Solution:
    def maxSum(self, g: List[List[int]]) -> int:
        p=[]
        m=0
        for i in range (len(g)):
            p.append([])
            for j in range (len(g[i])):
                if j==0:
                    p[i].append(g[i][j])
                elif j>0 and j<=2:
                    p[i].append(p[i][j-1]+g[i][j])
                elif j>2:
                    p[i].append(p[i][j-1]+g[i][j]-g[i][j-3])
        i=0
        while i<len(g)-2:
            j=2
            while j<len(g[0]):
                m=max(m,p[i][j]+g[i+1][j-1]+p[i+2][j])
                j+=1
            i+=1
        print(p) 
        return m

        