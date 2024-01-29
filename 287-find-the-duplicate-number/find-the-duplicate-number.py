class Solution:
    def findDuplicate(self, n: List[int]) -> int:
        a={}
        for i in n:
            if i in a:
                return i
            else:
                a[i]=0
               