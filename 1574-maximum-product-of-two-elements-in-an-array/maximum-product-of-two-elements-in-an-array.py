class Solution:
    def maxProduct(self, n: List[int]) -> int:
        n.sort()
        a=len(n)
        return (n[a-1]-1)*(n[a-2]-1)
        