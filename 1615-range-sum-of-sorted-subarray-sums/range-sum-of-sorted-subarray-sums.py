class Solution:
    def rangeSum(self, ns: List[int], n: int, l: int, r: int) -> int:
        a=[]
        j=1
        c=ns[0]
        a.append(c)
        while j<len(ns):
            c+=ns[j]
            a.append(c)
            k=c
            i=0
            while i<j:
                k-=ns[i]
                a.append(k)
                i+=1
            j+=1
        a.sort()
        return sum(a[l-1:r])%(10**9+7)

            


            