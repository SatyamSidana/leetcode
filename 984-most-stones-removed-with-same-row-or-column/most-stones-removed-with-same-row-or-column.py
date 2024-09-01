class Solution:
    def removeStones(self, s: List[List[int]]) -> int:
        p=[i for i in range(len(s))]
        r=[0]*len(s)
        def find(x):
            if x==p[x]:
                return x
            return (find(p[x]))
        def union(x,y):
            px=find(x)
            py=find(y)
            if px!=py:
                if r[px]>r[py]:
                    p[py]=px
                elif r[px]<r[py]:
                    p[px]=py
                else:
                    p[py]=px
                    r[px]+=1
        for i in range (len(s)):
            for j in range(i+1,len(s)):
                if s[i][0]==s[j][0] or s[i][1]==s[j][1]:
                    union(i,j)
        ans=set()
        for i in range(len(s)):
            ans.add(find(i))
        return len(s)-len(ans)