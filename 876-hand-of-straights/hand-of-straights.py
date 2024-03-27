class Solution:
    def isNStraightHand(self, h: List[int], g: int) -> bool:
        h.sort()
        if len(h)%g!=0:
            return False
        else:
            i=0
            a={}
            for i in range (len(h)):
                if a.get(h[i]):
                    a[h[i]].append(i)
                else:
                    a[h[i]]=[]
                    a[h[i]].append(i)
            for i in range (len(h)):
                if h[i]==-1:
                    pass
                else:
                    b=h[i]
                    for j in range (g):
                        print(b)
                        if a.get(b) and len(a[b])!=0:
                            c=a[b].pop(0)
                            h[c]=-1
                        else:
                            return False
                        b+=1                    
            return True        