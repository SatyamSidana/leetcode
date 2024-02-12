class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        a={}
        for i in s:
            c=sorted(list(i))
            b="".join(c)
            if b in a :
                a[b].append(i)
            else:
                a[b]=[i]
        b=[]
        for i in a:
            b.append(a[i])
        return b
        