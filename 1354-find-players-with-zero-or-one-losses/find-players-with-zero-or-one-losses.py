class Solution:
    def findWinners(self, m: List[List[int]]) -> List[List[int]]:
        a={}
        b={}
        c=[[],[]]
        for i in m:
            if i[0] not in a:
                b[i[0]]=1
            if i[1] not in a:
                a[i[1]]=0
            else:
                a[i[1]]+=1
        for i in b:
            if i not in a:
                c[0].append(i)
        for i in a:
            if a[i]==0:
                c[1].append(i)
        print(a,b)
        c[1].sort()
        c[0].sort()
        return c


        