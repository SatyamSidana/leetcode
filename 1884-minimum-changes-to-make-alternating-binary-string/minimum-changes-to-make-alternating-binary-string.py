class Solution:
    def minOperations(self, s: str) -> int:
        c=0
        m=0
        for i in range (len(s)):
            if i%2==1 and s[i]=="0":
                c+=1
            if i%2==0 and s[i]=="1":
                c+=1
        for i in range (len(s)):
            if i%2==0 and s[i]=="0":
                m+=1
            if i%2==1 and s[i]=="1":
                m+=1
        return min(m,c)
        