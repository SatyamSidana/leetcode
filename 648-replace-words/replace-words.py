class Solution:
    def replaceWords(self, d: List[str], s: str) -> str:
        a={}
        for i in d:
            a[i]=1
        s=list(s.split())
        c=""
        for i in range (len(s)):
            j=0
            while j<len(s[i]):
                if s[i][:j] in a:
                    s[i]=s[i][:j]
                    break
                j+=1
            c+=s[i]
            c+=" "
        return c[:len(c)-1]
