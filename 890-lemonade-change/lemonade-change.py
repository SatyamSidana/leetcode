class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a={}
        for i in bills:
            if i==5:
                if a.get(5):
                    a[5]+=1
                else:
                    a[5]=1
            elif i==10:
                if a.get(5) and a[5]>0:
                    a[5]-=1
                else:
                    return False
                if a.get(10):
                        a[10]+=1
                else:
                    a[10]=1
            else:
                if a.get(10) and a.get(5) and a[10]>0 and a[5]>0:
                    a[10]-=1
                    a[5]-=1
                elif a.get(5) and a[5]>2:
                    a[5]-=3
                else:
                    return False
        return True
        