class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a=""
        for i in s:
            a+=str((ord(i)-ord("a")+1))
        a=int(a)
        while k>0:
            c=0
            while a>0:
                c+=a%10
                a=a//10
            k-=1
            a=c
        return a