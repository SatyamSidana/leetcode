class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        b=0
        a=[0]*(len(nums)+1)
        for i in range (len(nums)):
            if nums[i]>len(nums) or nums[i]<1:
                pass
            else:
                a[nums[i]]=1
        for i in range (1,len(a)):
            if a[i]==0:
                b=i
                break
        if b==0:
            return len(nums)+1
        return b