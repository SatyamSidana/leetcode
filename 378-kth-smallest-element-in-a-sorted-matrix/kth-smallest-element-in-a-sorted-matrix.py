class Solution:
    def kthSmallest(self, m: List[List[int]], k: int) -> int:
        a=[]
        for i in m:
            for j in i:
                a.append(j)
        a.sort()
        return a[k-1]