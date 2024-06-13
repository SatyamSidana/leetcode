class Solution:
    def minCostClimbingStairs(self, c: List[int]) -> int:
        dp=[0]*(len(c)+1)
        for i in range (2,len(c)+1):
            dp[i]=min(c[i-1]+dp[i-1],c[i-2]+dp[i-2])
        print(dp)
        return dp[-1]