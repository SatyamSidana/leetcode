class Solution:
    def countHomogenous(self, a: str) -> int:
        c=0
        s=0
        e=0
        print(len(a))
        while(e<len(a)):
            if a[s]==a[e]:
                e+=1
            else:
                s=e
            c+=e-s
        return c%(10**9 + 7)
        