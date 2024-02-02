class Solution:
    def divideArray(self, n: List[int], k: int) -> List[List[int]]:
        a=[]
        n.sort()
        i=0
        while i <len(n)-2:
            if n[i+2]<=n[i]+k:
                b=[]
                b.append(n[i])
                b.append(n[i+1])
                b.append(n[i+2])
                a.append(b)
                i+=3
            else:
                return []
        return a

        