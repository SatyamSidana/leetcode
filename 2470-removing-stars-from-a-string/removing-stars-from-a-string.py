class Solution:
    def removeStars(self, s: str) -> str:
        a=[]
        for i in s:
            if i=="*" and len(a)!=0:
                a.pop()
            elif i!="*": 
                a.append(i)
        return "".join(a)
