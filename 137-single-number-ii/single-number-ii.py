class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a={}
        for i in nums:
            if a.get(i):
                a[i]+=1
            else:
                a[i]=1
            if a[i]==3:
                del a[i]
        for i in a:
            b=i
        return b
        