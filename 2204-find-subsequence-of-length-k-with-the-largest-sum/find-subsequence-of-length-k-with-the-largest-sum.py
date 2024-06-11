class Solution:
    def maxSubsequence(self, n: List[int], k: int) -> List[int]:
        a=[]
        for i in n:
            a.append(i)
        n.sort()
        if k==len(n):
            return a
        i=0
        j=len(n)-1
        s={}
        while k:
            if n[j] in s:
                s[n[j]]+=1
            else:
                s[n[j]]=1
            j-=1
            
            k-=1
        ans=[]
        for i in a:
            if s.get(i) and s[i]>0:
                ans.append(i)
                s[i]-=1
        return ans

