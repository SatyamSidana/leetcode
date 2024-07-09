class Solution:
    def averageWaitingTime(self, c: List[List[int]]) -> float:
        w=0
        t=0
        for i in c:
            if t>i[0]:
                w+=t-i[0]+i[1]
                t+=i[1]
            else:
                w+=i[1]
                t=i[0]+i[1]
        return w/len(c)