class Solution:
    def maxWidthOfVerticalArea(self, p: List[List[int]]) -> int:
        a=[]
        m=0
        for i in p:
            a.append(i[0])
        a.sort()
        for i in range (len(a)-1):
            m=max(m,a[i+1]-a[i])
        return m

        