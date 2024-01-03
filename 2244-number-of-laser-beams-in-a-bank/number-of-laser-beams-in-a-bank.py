class Solution:
    def numberOfBeams(self, b: List[str]) -> int:
        m=0
        s=0
        e=1
        while e<len(b):
            a=0
            c=0
            for i in b[s]:
                if i=="1":
                    a+=1
            for i in b[e]:
                if i=="1":
                    c+=1
            if c==0 and a!=0:
                e+=1
            else:
                m+=a*c
                s=e
                e+=1
        return m
