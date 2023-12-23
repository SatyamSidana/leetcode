class Solution:
    def numSpecial(self, m: List[List[int]]) -> int:
        a=defaultdict(int)
        b=defaultdict(int)
        c=0
        for i in range (len(m)):
            for j in range (len(m[0])):
                if m[i][j]==1:
                    a[i]+=1
                    b[j]+=1
        for i in range (len(m)):
            for j in range (len(m[0])):
                if m[i][j]==1:
                    if a[i]==1 and b[j]==1:
                        c+=1
        return c
                        
        

                



        