class Solution:
    def rob(self, n: List[int]) -> int:
        if len(n)==1:
            return n[0]
        if len(n)==2:
            return max(n[0],n[1])
        dp1=[0]*(len(n)-1)
        dp2=[0]*(len(n)-1)
        dp1[0]=n[0]
        dp1[1]=max(n[0],n[1])
        for i in range (2,len(n)-1):
            dp1[i]=max(n[i]+dp1[i-2],0+dp1[i-1])
        dp2[0]=n[1]
        dp2[1]=max(n[1],n[2])
        for i in range (2,len(n)-1):
            dp2[i]=max(n[i+1]+dp2[i-2],0+dp2[i-1])
        print(dp1,dp2)
        return max(dp1[-1],dp2[-1])
        
