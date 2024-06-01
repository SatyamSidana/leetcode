class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        b1=0
        b2=0
        x=0
        for i in nums:
            x=x^i
        r=x&-x
        for i in nums:
            if i& r:
                b1=b1^i
            else:
                b2=b2^i
        return [b1,b2]