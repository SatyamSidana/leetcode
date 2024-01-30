class Solution:
    def convert(self, s: str, n: int) -> str:
        m=""
        if n==1:
            return s
        if len(s)<=n:
            return s
        else:
            i=n
            a=[]
            for i in range (n):
                a.append([s[i]])
            print(a)
            c=1
            i=n
            r=n-2
            while i<len(s):
                if c==1:
                    while i<len(s) and r!=0:
                        a[r].append(s[i])
                        i+=1
                        r-=1
                    c=0
                if c==0:
                    r=0
                    while i<len(s) and r!=n:
                        a[r].append(s[i])
                        i+=1
                        r+=1
                    r=n-2
                    c=1
            print(a)
            for i in a:
                for j in i:
                    m+=j
            return m
