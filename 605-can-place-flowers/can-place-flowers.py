class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        i=0
        if len(f)==1 and f[i]==0:
            n-=1
        if n<=0:
            return True
        while i<len(f)-1:
            if i>0 and i<len(f)-2:
                if f[i]==f[i+1]==f[i+2]==0:
                    n-=1
                    i+=2
                else:
                    i+=1
            else:
                if f[i]==f[i+1]==0:
                    i+=1
                    n-=1
                else:
                    i+=1
            print(i,n)
            if n==0:
                return True
        
        return False
            
        