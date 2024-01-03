class Solution:
    def minimumRecolors(self, b: str, k: int) -> int:
        m=0
        s=0
        e=k
        for i in range (k):
            if b[i]=="W":
                m+=1
        c=m
        while e<len(b):
            if b[e]=="W":
                c+=1
            if b[s]=="W":
                c-=1
            print(c)
            m=min(c,m)
            e+=1
            s+=1
        return m
            
        