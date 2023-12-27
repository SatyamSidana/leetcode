class Solution:
    def intersect(self, n1: List[int], n2: List[int]) -> List[int]:
        a={}
        b=[]
        for i in n1:
            if a.get(i):
                a[i]+=1
            else:
                a[i]=1
        for i in n2 :
            if a.get(i) and a[i]!=0:
                b.append(i)
                a[i]-=1
        return b

