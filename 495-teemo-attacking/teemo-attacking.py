class Solution:
    def findPoisonedDuration(self, t: List[int], d: int) -> int:
        m=d
        for i in range (len(t)-1):
            m+=min(d,t[i+1]-t[i])
        return m


        
        