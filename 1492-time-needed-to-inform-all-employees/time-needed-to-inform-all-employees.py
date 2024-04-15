class Solution:
    def numOfMinutes(self, n: int, h: int, m: List[int], t: List[int]) -> int:
        a=[]
        b=[]
        c=0
        d=[]
        for i in range (len(m)):
            b.append([])
        for i in range (len(m)):
            if m[i]!=-1:
                b[m[i]].append(i)
        print(b)
        def dfs(r,c):
            c+=t[r]
            for i in b[r]:
                dfs(i,c)
            if len(b[r])==0:
                d.append(c)
            c-=t[r]
        dfs(h,c)
        
        return max(d)
