class Solution:
    def findPoisonedDuration(self, t: List[int], d: int) -> int:
        m=0
        for i in range (len(t)-1):
            m+=min(d,t[i+1]-t[i])
        m+=d
        return m


        
        