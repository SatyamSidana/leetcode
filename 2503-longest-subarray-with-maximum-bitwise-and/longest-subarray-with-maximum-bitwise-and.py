class Solution:
    def longestSubarray(self, n: List[int]) -> int:
        m=max(n)
        a=0
        i=0
        while i<len(n):
            j=0
            while i<len(n) and n[i]==m:
                i+=1
                j+=1
            a=max(a,j)
            i+=1
        return a