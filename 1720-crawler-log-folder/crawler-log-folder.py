class Solution:
    def minOperations(self, l: List[str]) -> int:
        a=0
        for i in l:
            if i=="../" and a>0:
                a-=1
            elif i!="./" and i!="../":
                a+=1
        return a
        