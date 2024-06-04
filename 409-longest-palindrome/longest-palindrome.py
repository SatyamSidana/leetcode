class Solution:
    def longestPalindrome(self, s: str) -> int:
        a={}
        c=0
        for i in s:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in a:
            c+=(a[i]//2)*2
        if c<len(s):
            return c+1
        return c
        