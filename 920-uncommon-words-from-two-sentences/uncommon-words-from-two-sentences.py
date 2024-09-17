class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a=s1.split()+s2.split()
        d1={}
        ans=[]
        for i in a:
            if i in d1:
                d1[i]=-1
            else:
                d1[i]=1
        for i in d1:
            if d1[i]==1:
                ans.append(i)
        return ans