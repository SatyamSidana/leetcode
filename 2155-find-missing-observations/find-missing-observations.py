class Solution:
    def missingRolls(self, r: List[int], mean: int, n: int) -> List[int]:
        m=sum(r)
        need=mean*(n+len(r))-m
        print(need)
        ans=[1]*n
        need-=n
        if need<0:
            return []
        x=(need+n)//n
        ans=[x]*n
        for i in range(need%n):
            ans[i]+=1
        if ans[0]>6:
            return []
        return ans
        while need>0 and c<6:
            for i in range (min(need,n)):
                ans[i]+=1
                need-=1
            c+=1
        if need>0:
            return []
        return ans