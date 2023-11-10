class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a=0
        b=0
        for i in range  (len(s)):
            a+=ord(s[i])
            b+=ord(t[i])
        b+=ord(t[len(t)-1])
        return chr(b-a)