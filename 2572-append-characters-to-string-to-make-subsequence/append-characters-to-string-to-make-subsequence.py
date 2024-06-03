class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        c=0
        e=0
        st=0
        j=0
        while e<len(s) and j<len(t):
            
            if s[e]==t[j]:
                while e<len(s) and j<len(t) and s[e]==t[j]:
                    e+=1
                    j+=1
                print(c)
                st=e
            else:
                e+=1
                st+=1
        return len(t)-j