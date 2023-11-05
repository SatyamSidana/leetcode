class Solution:
    def findMaxAverage(self, n: List[int], k: int) -> float:
        maxav=0
        a=0
        for i in range (k):
            maxav+=n[i]
        a=maxav
        for i in range (0,len(n)-k):
            a=a-n[i]+n[k+i]
            maxav=max(maxav,a)
        return maxav/k


        