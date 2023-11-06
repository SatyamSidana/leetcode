class Solution:
    def subarraySum(self, n: List[int], k: int) -> int:
        c=0
        w=0
        a=defaultdict(int)
        a[0]=1
        for i in n:
            w+=i
            c+=a[w-k]
            a[w]+=1

        return c











 
        

        