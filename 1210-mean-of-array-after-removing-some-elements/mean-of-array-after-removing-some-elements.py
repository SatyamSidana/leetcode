class Solution:
    def trimMean(self, a: List[int]) -> float:
        a.sort()
        b=ceil(len(a)*.05)
        print(b)
        for i in range (b):
            a.pop()
            a.pop(0)
        return sum(a)/len(a)
        