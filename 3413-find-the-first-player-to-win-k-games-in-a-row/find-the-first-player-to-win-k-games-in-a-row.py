class Solution:
    def findWinningPlayer(self, s: List[int], k: int) -> int:
        ans=-1
        c=0
        q=[]
        if k>=len(s):
            a=max(s)
            return s.index(a)
        f=[0]*len(s)
        for i in range (len(s)):
            q.append(i)
        while c<k :
            a=q[0]
            b=q[1]
            if s[a]>s[b]:
                ans=a
                if f[a]==1:
                    c+=1
                else:
                    c=1
                    f[a]=1
                q.pop(1)
                q.append(b)
                f[b]=0
            else:
                ans=b
                if f[b]==1:
                    c+=1
                else:
                    c=1
                    f[b]=1
                q.pop(0)
                q.append(a)
                f[a]=0
        return ans