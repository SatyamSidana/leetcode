class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        a=""
        while i<len(s):
            j=0
            if i+k > len(s):
                k=len(s)-i
                c=len(s)-1
                while j<k and i<len(s):
                    a+=s[c]
                    c-=1
                    j+=1
                    i+=1
            else:
                c=i+k-1
                while j<k and i<len(s):
                    a+=s[c]
                    c-=1
                    j+=1
                    i+=1
            j=0
            while j<k and i<len(s):
                a+=s[i]
                i+=1
                j+=1
        return a
                
            
