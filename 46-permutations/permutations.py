class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def dfs(p,n):
            if not n:
                ans.append(p)
                return 0
            for i,a in enumerate(n):
                dfs(p+[a],n[:i]+n[i+1:])
        dfs([],nums)
        return ans