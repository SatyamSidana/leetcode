class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        b={}
        for i in range (len(s)):
            if b.get(t[i]):
                if s[i]!=b[t[i]]:
                    return False
            else:
                for j in range (len(b)):
                    if s[i]==b[t[j]]:
                        return False
                b[t[i]]=s[i]    
        return True