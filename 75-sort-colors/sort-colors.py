class Solution:
    def sortColors(self, n: List[int]) -> None:
        a=len(n)
        i=0
        c=0
        k=0
        while k<a:
            if n[k]==0:
                n[i]=0
                i+=1
            elif n[k]==2:
                n.append(2)
                c+=1
            k+=1
        for x in range (c):
            
            n.pop(i)
        
        k=0
        print(len(n)-c-i)
        b=i
        while i<a and k<len(n)-c-b:
            n[i]=1
            i+=1
            k+=1
        
        
        