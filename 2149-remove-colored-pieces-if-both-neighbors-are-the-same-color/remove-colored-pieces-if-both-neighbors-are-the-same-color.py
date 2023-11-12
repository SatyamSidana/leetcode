class Solution:
    def winnerOfGame(self, c: str) -> bool:
        i=0
        a=0
        b=0
        if len(c)==1 or len(c)==2:
            return False
        while i<len(c)-2:
            if c[i]==c[i+1]==c[i+2]=="A":
                a+=1
            if c[i]==c[i+1]==c[i+2]=="B":
                b+=1
            i+=1
        if a>b:
            return True
        return False    


        