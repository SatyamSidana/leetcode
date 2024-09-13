class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def dfs(p,n):
            if not n:
                res.append(p)
                return 0
            for i in range (len(n)):
                if i>0 and n[i]==n[i-1]:
                    continue
                else:
                    dfs(p+[n[i]],n[:i]+n[i+1:])
        dfs([],nums)
        return res