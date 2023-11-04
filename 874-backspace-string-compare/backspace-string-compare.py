class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in s:
            if i=="#" and len(a)!=0:
                a.pop()
            elif i=="#" and len(a)==0:
                pass
            else:
                a.append(i)
        for i in t:
            if i =="#" and len(b)!=0:
                b.pop()
            elif i =="#" and len(b)==0:
                pass
            else:
                b.append(i)
        if a==b:
            return True
        else:
            return False

        