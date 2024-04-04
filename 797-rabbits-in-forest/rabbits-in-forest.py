class Solution:
    def numRabbits(self, a: List[int]) -> int:
        d={}
        c=0
        for i in a:
            if d.get(i):
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if i+1>=d[i]:
                c+=i+1
            else:
                if i==0:
                    c+=d[i]
                else:
                    if d[i]%(i+1)==0:
                        t=0
                    else:
                        t=1
                    c+=(d[i]//(i+1)+t)*(i+1)
        return c
        