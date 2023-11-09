class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        a=s.split()
        b={}
        if len(p)!=len(a):
            return False
        for i in range (len(a)):
            if b.get(p[i]):
                if a[i]!=b[p[i]]:
                    return False
            else:
                print(b)
                for j in range (len(b)):
                    if a[i]==b[p[j]]:
                        return False
                b[p[i]]=a[i]
        print(b)
        return True

        