class Solution:
    def isPathCrossing(self, p: str) -> bool:
        a={(0,0)}
        x,y=0,0
        for i in p:
            if i=="N":
                y+=1    
            elif i=="S":
                y-=1
            elif i=="E":
                x+=1
            elif i=="W":
                x-=1
            if (x,y) in a: 
                return True
            a.add((x,y))
        return False   

        
        