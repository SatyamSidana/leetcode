class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        e=0
        j=0
        while e<len(s) and j<len(t):
            
            if s[e]==t[j]:
                while e<len(s) and j<len(t) and s[e]==t[j]:
                    e+=1
                    j+=1
            else:
                e+=1
        return len(t)-j