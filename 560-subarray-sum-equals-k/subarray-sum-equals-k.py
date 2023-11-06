class Solution:
    def subarraySum(self, n: List[int], k: int) -> int:
        c=0
        w=0
        a={}
        a[0]=1
        for i in n:
            w+=i
            if a.get(w-k):
                c+=a[w-k]
            if a.get(w):
                a[w]+=1
            else:
                a[w]=1

        return c











 
        

        