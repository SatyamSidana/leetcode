class Solution:
    def validStrings(self, n: int) -> List[str]:
        a=[]
        def f(s,c):
            m=0
            if c==n:
                a.append(s)
                return 1
            if c>n:
                return -1
            s+="1"
            c+=1
            f(s,c)
            s=s[0:len(s)-1]
            c-=1
            if len(s)==0:
                s+="0"
                c+=1
                f(s,c)
                
            else:
                if s[-1]=="1":
                    s+="0"
                    c+=1
                    f(s,c)
                    
            return m
        f("",0)
        return list(a)