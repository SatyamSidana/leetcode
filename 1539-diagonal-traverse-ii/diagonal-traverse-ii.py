class Solution:
    def findDiagonalOrder(self, n: List[List[int]]) -> List[int]:
        a=[]
        b=defaultdict(list)
        for i in range (len(n)):
            for j in range (len(n[i])):
                b[i+j].append(j)
        print(b)
        for i in range (len(b)):
            c=b[i]
            c.sort()
            print(c)
            for j in c:
                a.append(n[i-j][j])
        return a



        