
class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        n=len(m)
        if len(m) == 1:
            return min(m[0])
        
        if len(m[0]) == 1:
            return sum(row[0] for row in m)
        
        dp = [[-1 for _ in range(len(m[0]))] for _ in range(len(m))]
        for i in range (len(m[0])):
            dp[len(m)-1][i]=m[len(m)-1][i]
        for i in range (2,len(m)+1):
            for j in range (len(m)):
                if j==0:
                    dp[n-i][j]=min(dp[n-i+1][j],dp[n-i+1][j+1])+m[n-i][j]
                elif j==n-1:
                    dp[n-i][j]=min(dp[n-i+1][j],dp[n-i+1][j-1])+m[n-i][j]
                else:
                    dp[n-i][j]=min(dp[n-i+1][j],dp[n-i+1][j+1],dp[n-i+1][j-1])+m[n-i][j]
        return min(dp[0])
