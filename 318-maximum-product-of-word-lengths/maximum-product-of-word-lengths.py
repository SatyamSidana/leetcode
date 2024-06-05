class Solution:
    def maxProduct(self, w: List[str]) -> int:
        a={}
        m=0
        for i in range (26):
            a[chr(ord("a")+i)]=1<<i
        b=[]
        for i in w:
            c=0
            for j in i:
                c=c|(a[j])
            b.append(c)
        for i in range (len(b)):
            for j in range (i+1,len(b)):
                if b[i]&b[j]==0:
                    m=max(m,len(w[i])*len(w[j]))
        return m