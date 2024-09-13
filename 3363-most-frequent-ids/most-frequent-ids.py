from heapq import heappush, heappop
from collections import Counter
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        h=[]
        count=Counter()
        res=[]
        for i,f in zip(nums,freq):
            count[i]+=f
            heappush(h,[-count[i],i])
            while count[h[0][1]]!=-h[0][0]:
                heappop(h)
            res.append(-h[0][0])
        return res