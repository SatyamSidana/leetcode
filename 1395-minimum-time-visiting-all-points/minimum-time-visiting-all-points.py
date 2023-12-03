class Solution:
    def minTimeToVisitAllPoints(self, p: List[List[int]]) -> int:
        m=0
        for i in range (len(p)-1):
            m+=max(abs(p[i][0]-p[i+1][0]),abs(p[i][1]-p[i+1][1]))
        return m

        