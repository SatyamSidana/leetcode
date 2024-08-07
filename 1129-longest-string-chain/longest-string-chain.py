class Solution:
    def longestStrChain(self, w: List[str]) -> int:
        a={}
        for i in w:
            a[i]=1
        w.sort(reverse=True)
        dp={}
        def f(s,i):
            if i==len(s):
                return 0
            if (s,i) in dp:
                return dp[(s,i)]
            r=(s[:i]+s[i+1:])
            if r in a:
                x=max(1+f(r,0),f(s,i+1))
            else:
                x=f(s,i+1)
            dp[(s,i)]=x
            return x
        m=0
        for i in w:
            m=max(m,f(i,0))
        return m+1