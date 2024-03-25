class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a={}
        d=0
        for i in nums:
            if a.get(i):
                a[i]+=1
            else:
                a[i]=1
        b=list(a.values())
        b.sort()
        c=b[-1]
        i=len(b)-1
        while i>=0:
            if b[i]==c:
                d+=c
            else:
                break
            i-=1
        return d

        