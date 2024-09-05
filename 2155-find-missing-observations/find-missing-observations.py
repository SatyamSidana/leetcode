class Solution:
    def missingRolls(self, r: List[int], mean: int, n: int) -> List[int]:
        m=sum(r)
        need=mean*(n+len(r))-m
        ans=[1]*n
        need-=n
        if need<0:
            return []
        c=1
        while need>0 and c<6:
            for i in range (min(need,n)):
                ans[i]+=1
                need-=1
            c+=1
        if need>0:
            return []
        return ans