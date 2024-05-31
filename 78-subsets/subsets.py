class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        sub=2**len(nums)
        for i in range (sub):
            l=[]
            for j in range (len(nums)):
                if i&(1<<j):
                    l.append(nums[j])
            ans.append(l)
        return ans