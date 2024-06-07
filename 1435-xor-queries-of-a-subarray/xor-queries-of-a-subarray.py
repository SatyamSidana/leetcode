class Solution:
    def xorQueries(self, a: List[int], q: List[List[int]]) -> List[int]:
        ans=[]
        p=[]
        p.append(a[0])
        for i in range (1,len(a)):
            p.append((p[i-1])^a[i])
        for i in q:
            if i[0]==i[1]:
                r=ans.append(a[i[0]])
            else:
                if i[0]==0:
                    ans.append(p[i[1]])
                else:
                    ans.append(p[i[1]]^p[i[0]-1])

        return ans