class Solution:
    def maxSubarrayLength(self, n: List[int], k: int) -> int:
        a={}
        s=0
        e=0
        m=0
        while e<len(n):
            if a.get(n[e]):
                a[n[e]]+=1
            else:
                a[n[e]]=1
            while a[n[e]]>k:
                a[n[s]]-=1
                s+=1
            e+=1
            m=max(m,e-s)        
        return m        