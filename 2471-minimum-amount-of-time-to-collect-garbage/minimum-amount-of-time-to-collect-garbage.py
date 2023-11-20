class Solution:
    def garbageCollection(self, g: List[str], t: List[int]) -> int:
        m=0
        p=0
        gg=0
        peekGarbageTime = endM = endP = endG = 0
        i = len(g) - 1
        while i >=0:
            peekGarbageTime += len(g[i])
            if not endM and 'M' in g[i]: endM = i
            if not endP and 'P' in g[i]: endP = i
            if not endG and 'G' in g[i]: endG = i
            i -= 1

        for i in range (len(g)):
            for j in g[i]:
                if j=="M":
                    m+=1
                if j=="G":
                    gg+=1
                if j=="P":
                    p+=1
            if i<len(g)-1:
                if i<endM:
                    m+=t[i]
                if i<endG:
                    gg+=t[i]
                if i<endP:
                    p+=t[i]
        return m+gg+p
            

                


        