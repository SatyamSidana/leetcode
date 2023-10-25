class Solution:
    def majorityElement(self, n: List[int]) -> List[int]:
        a={}
        b=[]
        for i in n:
            if i in a:
                a[i]=a.get(i)+1
            else:
                a[i]=1
        for i in a:
            if a.get(i)>(len(n)/3):
                b.append(i)
        return(b)