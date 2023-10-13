class Solution:
    def firstUniqChar(self, s: str) -> int:
        a={}
        for i in range (len(s)):
            if s[i] in a:
                a.update({s[i]:-1})
            else:
                a[s[i]]=i
        b=list(a.values())
        for i in b:
            if i!=-1:
                return i

        return -1
        