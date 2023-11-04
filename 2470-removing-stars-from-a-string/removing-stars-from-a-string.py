class Solution:
    def removeStars(self, s: str) -> str:
        a=[]
        b=""
        for i in s:
            if i=="*" and len(a)!=0:
                a.pop()
            elif i!="*": 
                a.append(i)
        for i in a:
            b+=i
        return b
