class Solution:
    def minMovesToSeat(self, se: List[int], s: List[int]) -> int:
        c=0
        s.sort()
        se.sort()
        for i in range (len(s)):
            c+=abs(s[i]-se[i])
        return c