class Solution:
    def combinationSum2(self, c: List[int], t: int) -> List[List[int]]:
        ans={}
        c.sort()
        def f(i,s,a):
            if s==t:
                tuple(a)
                ans[a]=1
                return 1 
            if s>t or i==len(c):
                return 1
            for j in range(i,len(c)):
                if (j>i and c[j]==c[j-1]):
                    continue    
                f(j+1,s+c[j],a+(c[j],))
        b=[]
        f(0,0,())
        res=[]
        for i in ans:
            res.append(list(i))
        return res



