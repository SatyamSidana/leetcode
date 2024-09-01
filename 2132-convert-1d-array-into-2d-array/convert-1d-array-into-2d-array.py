class Solution:
    def construct2DArray(self, o: List[int], m: int, n: int) -> List[List[int]]:
        if len(o)!=m*n:
            return []
        i=0
        ans=[]
        while i<len(o):
            a=[]
            for j in range (i,i+n):
                a.append(o[j])
            ans.append(a)
            i+=n
        return ans