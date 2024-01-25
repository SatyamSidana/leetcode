class Solution:
    def halvesAreAlike(self, n: str) -> bool:
        a={"a":1,"e":1,"i":1,"o":1,"u":1,"A":1,"E":1,"I":1,"O":1,"U":1}
        c=0
        for i in range (len(n)//2):
            if a.get(n[i]):
                c+=1
        for i in range (len(n)//2,len(n)):
            if a.get(n[i]):
                c-=1
        if c==0:
            return True
        return False

        