class Solution:
    def removeDuplicates(self, s: str) -> str:
        a=[]
        b=""
        a.append(s[0])
        i=1
        while i<len(s):
            while a and s[i]==a[-1]:
                a.pop()
                i+=1
                if i >=len(s):
                    break
            if i <len(s):
                a.append(s[i])
            i+=1
            
        for i in a:
            b+=i
        return b
            
        