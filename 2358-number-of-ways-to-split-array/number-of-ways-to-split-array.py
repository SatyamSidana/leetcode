class Solution:
    def waysToSplitArray(self, n: List[int]) -> int:
        ps=list()
        b=len(n)
        ss=[None]*b
        c=0
        for i in range (len(n)):
            if i==0:
                ps.append(n[0])
            else:
                ps.append(n[i]+ps[i-1])
        i=len(n)-1

        while(i>=0):
            if i==len(n)-1:
                ss[i]=0
                
            else:
                ss[i]=n[i+1]+ss[i+1]
            
            i-=1

        for i in range (len(n)-1):
            if ps[i]>=ss[i]:
                c+=1

    
        return c
        