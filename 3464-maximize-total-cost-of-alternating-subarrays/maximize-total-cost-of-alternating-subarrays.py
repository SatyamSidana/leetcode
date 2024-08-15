class Solution:
    def maximumTotalCost(self, n: List[int]) -> int:
        c=len(n)
        dp =[[0,0] for i in range(c)]
        dp[0][0]=n[0]
        dp[0][1]=n[0]
        for i in range (1,c):
            dp[i][0]=max(dp[i-1][1],dp[i-1][0])+n[i]
            dp[i][1]=dp[i-1][0]-n[i]
        return max(dp[c-1][0],dp[c-1][1])

            
