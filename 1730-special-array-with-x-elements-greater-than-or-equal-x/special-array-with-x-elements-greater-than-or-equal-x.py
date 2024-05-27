class Solution:
    def specialArray(self, n: List[int]) -> int:
        n.sort()
        i=0
        j=0
        while i<=len(n) and j<len(n):
            if n[j]>=i and len(n)-j==i:
                return i 
            if i<=n[j]:
                i+=1
            else:
                j+=1
            if i>len(n)-j:
                break
            
        return -1