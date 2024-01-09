class Solution:
    def longestOnes(self, n: List[int], k: int) -> int:
        e=0
        s=0
        z=[]
        i=0
        c=0
        while c<k and e<len(n):
            if n[e]==0:
                c+=1
                z.append(e)
            e+=1
        m=e-s
        while e<len(n):
            if n[e]==0:
                m=max(m,e-s)
                z.append(e)
                s=z[i]+1
                i+=1
            e+=1
            m=max(e-s,m)
            print(s,e)
        print(z)
        
        return m