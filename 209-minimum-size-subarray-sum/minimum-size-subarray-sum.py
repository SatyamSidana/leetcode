class Solution:
    def minSubArrayLen(self, t: int, n: List[int]) -> int:
        s=0
        e=0
        w=0
        minl=10**5+1
        while(e<len(n)):
            w+=n[e]
            e+=1
            while s<e and w>=t :
                minl=min(minl,e-s)
                w-=n[s]
                s+=1
        if minl==10**5+1:
            return 0
        return minl
            


        