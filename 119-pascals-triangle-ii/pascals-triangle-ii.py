class Solution:
    def getRow(self, n: int) -> List[int]:
        if n==0:
            return [1]
        ans=[[1],[1,1]]
        if n==1:
            return [1,1]
        for i in range (2,n+1):
            ans.append([1])
            for j in range (1,i):
                ans[i].append(ans[i-1][j-1]+ans[i-1][j])
            ans[i].append(1)
        return ans[-1]