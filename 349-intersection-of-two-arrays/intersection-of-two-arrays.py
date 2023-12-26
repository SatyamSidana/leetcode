class Solution:
    def intersection(self, n1: List[int], n2: List[int]) -> List[int]:
        a=set()
        b={}
        for i in n1:
            b[i]=1
        for i in n2:
            if b.get(i):
                a.add(i)
        return list(a)

        