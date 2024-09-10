class Solution:
    def maxScore(self, g: List[List[int]]) -> int:
        res=-inf
        n=len(g[0])
        m=len(g)
        for i in range(m):
            for j in range(n):
                prev= min(g[i-1][j] if i else inf,g[i][j-1] if j else inf)
                res=max(res,g[i][j]-prev)
                g[i][j]=min(prev,g[i][j])
        return res