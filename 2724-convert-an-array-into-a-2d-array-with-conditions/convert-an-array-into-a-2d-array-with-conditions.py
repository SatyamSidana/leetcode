class Solution:
    def findMatrix(self, n: List[int]) -> List[List[int]]:
        b={}
        for i in n:
            if b.get(i):
                b[i]+=1
            else:
                b[i]=1
        e=max(b.values())
        print(e)
        a=[]
        for i in range (e):
            a.append([])
        for i in b:
            for j in range (b[i]):
                a[j].append(i)
        return a
        