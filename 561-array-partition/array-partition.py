class Solution:
    def arrayPairSum(self, n: List[int]) -> int:
        n.sort()
        i=0
        c=0
        while i<len(n):
            c+=n[i]
            i+=2
        return c


        