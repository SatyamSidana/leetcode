class Solution:
    def findSpecialInteger(self, a: List[int]) -> int:
        d=0.25*len(a)
        c=0
        b=0
        if len(a)==1:
            return a[0]
        for i in a:
            if i==b:
                c+=1
                if c>d:
                    return i
            else:
                b=i
                c=1
            


        