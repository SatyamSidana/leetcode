class Solution:
    def majorityElement(self, n: List[int]) -> int:
        a={}
        for i in n:
            if i in a:
                a[i]=a.get(i)+1
            else:
                a[i]=1
            if a.get(i)>len(n)/2:
                return i

        