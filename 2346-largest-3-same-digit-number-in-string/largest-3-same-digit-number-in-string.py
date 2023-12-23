class Solution:
    def largestGoodInteger(self, n: str) -> str:
        c=0
        a=[]
        i=0
        while i<len(n)-2: 
            if n[i]==n[i+1] and n[i]==n[i+2]:
                a.append(n[i])
                i+=3
            else:
                i+=1
        if len(a)==0:
            return ""
        return max(a)*3
        