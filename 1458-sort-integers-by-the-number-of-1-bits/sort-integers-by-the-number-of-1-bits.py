class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        return map(lambda x : x[1], sorted(map(lambda x : (bin(x).count('1'), x), arr)))
                    
        