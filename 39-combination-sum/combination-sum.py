class Solution:
    def combinationSum(self, c: List[int], ta: int) -> List[List[int]]:
        s=[]
        a=[]
        def ans(i,t,a):
            if i==len(c):
                if t==0:
                    s.append(list(a))
                return None
            if c[i]<=t:
                t-=c[i]
                a.append(c[i])
                ans(i,t,a)
                t+=c[i]
                a.remove(c[i])
                ans(i+1,t,a)
            else:
                ans(i+1,t,a)
        ans(0,ta,a)
        return list(s)
