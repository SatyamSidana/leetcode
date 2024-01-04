class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        a={}
        b={}
        for i in range (len(m)):
            for j in range (len(m[0])):
                if m[i][j]==0:
                    a[i]=1
                    b[j]=1
        for i in a:
            for j in range (len(m[0])):
                m[i][j]=0
        for i in b:
            for j in range (len(m)):
                m[j][i]=0
        print(a,b)

        
        