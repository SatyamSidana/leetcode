class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a=[0,0]
        for i in bills:
            if i==5:
                a[0]+=1
            elif i==10:
                if a[0]>0:
                    a[0]-=1
                else:
                    return False
                a[1]+=1
            else:
                if a[1]>0 and a[0]>0:
                    a[1]-=1
                    a[0]-=1
                elif a[0]>2:
                    a[0]-=3
                else:
                    return False
        return True
        