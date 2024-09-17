class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a=s1.split()
        b=s2.split()
        d1={}
        d2={}
        ans=[]
        for i in a:
            if i in d1:
                d1[i]=-1
            else:
                d1[i]=1
        for i in b:
            if i in d2:
                d2[i]=-1
            else:
                d2[i]=1
        for i in d1:
            if i in d2:
                d1[i]=-1
                d2[i]=-1
        for i in d2:
            if d2[i]==1:
                ans.append(i)
        for i in d1:
            if d1[i]==1:
                ans.append(i)
        return ans