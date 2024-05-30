class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        a={}
        for i in nums:
            a[i]=1
        m=-1
        for i in nums:
            if a.get(-i):
                m=max(i,m)
        return m 