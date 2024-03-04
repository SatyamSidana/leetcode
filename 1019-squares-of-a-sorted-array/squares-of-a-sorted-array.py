class Solution:
    def sortedSquares(self, n: List[int]) -> List[int]:
        a=[]
        for i in n:
            a.append(i*i)
        a.sort()
        return a
                
        