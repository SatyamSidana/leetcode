class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        m=-1
        a={}
        for i in range (len(s)):
            if s[i] in a:
                m=max(m,i-a[s[i]]-1)
                #a[s[i]]=i
            else:
                a[s[i]]=i
        return m
        