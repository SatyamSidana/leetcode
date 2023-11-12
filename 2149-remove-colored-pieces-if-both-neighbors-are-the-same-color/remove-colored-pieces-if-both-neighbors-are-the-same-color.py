class Solution:
    def winnerOfGame(self, c: str) -> bool:
        e=0
        s=0
        n=0
        if len(c)==1 or len(c)==2:
            return False
        while e<len(c):
            while c[e]==c[s] and e<len(c):
                e+=1
                if e==len(c):
                    break
            if e-s>=3 :
                if c[s]=="A":
                    n+=e-s-2
                else:
                    n-=e-s-2
            print(n)
            s=e            
        if n>0:
            return True
        return False    


        