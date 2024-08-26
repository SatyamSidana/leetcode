class Solution:
    def checkRecord(self, s: str) -> bool:
        for i in range (len(s)-2):
            if s[i:i+3]=="LLL":
                return False
        c=0
        for i in s:
            if i=="A":
                c+=1
        return c<2