class Solution:
    def rob(self, n: List[int]) -> int:
        if len(n)==1:
            return n[0]
        dp=[0]*len(n)
        dp[0]=n[0]
        dp[1]=(max(n[0],n[1]))
        for i in range (2,len(n)):
            dp[i]=max(dp[i-1],n[i]+dp[i-2])
        return dp[-1]