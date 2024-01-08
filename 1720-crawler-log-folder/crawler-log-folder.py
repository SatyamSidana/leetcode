class Solution:
    def minOperations(self, l: List[str]) -> int:
        a=[]
        for i in l:
            if i=="../" and len(a)>0:
                a.pop()
            elif i!="./" and i!="../":
                a.append(i)
        return len(a)
        