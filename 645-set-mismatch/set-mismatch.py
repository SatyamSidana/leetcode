class Solution:
    def findErrorNums(self, n: List[int]) -> List[int]:
        a={}
        b=[]
        for i in range (len(n)) :
            if a.get(n[i]):
                b.append(n[i])
            else:
                a[n[i]]=1
        for i in range (1,len(n)+1):
            if a.get(i):
                pass
            else:
                b.append(i)
                break
        return b
        