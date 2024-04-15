class Solution:
    def minCostToMoveChips(self, p: List[int]) -> int:
        b=[]
        a=0
        r=0
        for i in p:
            if i%2==0:    
                a+=1
            else:
                a-=1
        if a>=0:
            for i in p:
                if i%2==1:
                    r+=1
        else:
            for i in p:
                if i%2==0:
                    r+=1
        
        return r
        