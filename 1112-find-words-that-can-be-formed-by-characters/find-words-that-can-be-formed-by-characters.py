class Solution:
    def countCharacters(self, w: List[str], c: str) -> int:
        n=0 
        for i in w:
            a=defaultdict(int)
            for s in c:
                a[s]+=1
            co=0
            for j in i:
                if a.get(j):
                    if a[j]>0:
                        a[j]-=1
                        co+=1
                    else:
                        break
                else:
                    break
            if co==len(i):
                n+=len(i)
            print(a)
        return n
            
        