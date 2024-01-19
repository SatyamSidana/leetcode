class Solution:
    def chalkReplacer(self, c: List[int], k: int) -> int:
        m=k%sum(c)
        i=0
        while m>0 and i<len(c):
            m-=c[i]
            i+=1
        if m<0:
            return i-1
        return i
        