class Solution:
    def numSubarraysWithSum(self, n: List[int], goal: int) -> int:
        p=[]
        p.append(n[0])
        c=0
        for i in range (len(n)-1):
            p.append(p[i]+n[i+1])
        a={}
        a[0]=1
        for i in p:
            if a.get(i-goal):
                c+=a[i-goal]
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        return c


