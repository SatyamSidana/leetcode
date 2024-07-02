class Solution:
    def canJump(self, n: List[int]) -> bool:
        if len(n)==1:
            return True
        if n[0]==0:
            return False
        dp=[0]*len(n)
        dp[0]=n[0]
        for i in range (1,len(dp)-1):
            dp[i]=max(n[i],dp[i-1]-1)
            if dp[i]==0:
                return False
        return True
                
        