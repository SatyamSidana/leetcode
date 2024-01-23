class Solution:
    def trimMean(self, a: List[int]) -> float:
        a.sort()
        b=ceil(len(a)*.05)
        a=a[b:len(a)-b]
        return sum(a)/len(a)
        