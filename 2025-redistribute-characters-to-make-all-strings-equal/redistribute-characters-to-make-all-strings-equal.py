class Solution:
    def makeEqual(self, w: List[str]) -> bool:
        a={}
        for i in w:
            for j in i:
                if j in a:
                    a[j]+=1
                else:
                    a[j]=1
        t=True
        for i in a:
            if a[i]%(len(w))!=0:
                return False
        return t
        

        