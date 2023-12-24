class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        for i in s:
            if a.get(i):
                a[i]+=1
            else:
                a[i]=1
        for i in t:
            if a.get(i):
                if a[i]==0:
                    return False 
                else:
                    a[i]-=1
                    if a[i]==0:
                        del a[i]
            else:
        
                return False
        if len(a)!=0:
            return False
        return True 
        