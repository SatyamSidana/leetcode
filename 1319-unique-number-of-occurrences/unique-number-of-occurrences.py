class Solution:
    def uniqueOccurrences(self, a: List[int]) -> bool:
        b={}
        c=set()
        for i in a:
            if b.get(i):
                b[i]+=1
            else:
                b[i]=1
        for i in b:
            c.add(b[i])
        if len(b)!=len(c):
            return False
        return True


        