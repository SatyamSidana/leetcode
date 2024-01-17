class Solution:
    def uniqueOccurrences(self, a: List[int]) -> bool:
        b={}
        c={}
        for i in a:
            if b.get(i):
                b[i]+=1
            else:
                b[i]=1
        for i in b:
            if c.get(b[i]):
                return False
            c[b[i]]=1
        return True


        