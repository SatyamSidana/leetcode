class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        a=[]
        b=""
        a.append([s[0],1])
        i=1
        while i<len(s):
            if a and s[i]==a[-1][0]:
                a[-1][1]+=1
                if a[-1][1]==k:
                    a.pop()
            else:
                a.append([s[i],1])
            i+=1
        for i in a:
            b+=i[0]*i[1]
        return b
            

                
            
        
        