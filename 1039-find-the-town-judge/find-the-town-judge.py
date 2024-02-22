class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        if n==1 and t==[]:
            return 1 
        a={}
        b={}
        for i in t:
            if a.get(i[1]):
                a[i[1]]+=1
            else:
                a[i[1]]=1
            b[i[0]]=1
        for i in a:
            if a[i]==n-1 :
                if b.get(i):
                    pass
                else:
                    return i                
        return -1       