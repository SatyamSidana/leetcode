class Solution:
    def transpose(self, m: List[List[int]]) -> List[List[int]]:
        a=[]
        j=0
        while j<len(m[0]):
            i=0
            b=[]
            while i<len(m):
                b.append(m[i][j])
                i+=1
            a.append(b)
            j+=1
        return a

            

        