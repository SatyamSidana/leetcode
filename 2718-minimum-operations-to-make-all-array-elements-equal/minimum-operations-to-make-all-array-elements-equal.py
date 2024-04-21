class Solution:
    def minOperations(self, n: List[int], q: List[int]) -> List[int]:
        a=[]
        p=[]
        n.sort()
        p.append(n[0])
        for i in range (1,len(n)):
            p.append(n[i]+p[i-1])
        for i in q:
            l=0
            h=len(n)-1
            while l<=h:
                mid=(l+h)//2
                if n[mid]<i:
                    l=mid+1
                elif n[mid]>i:
                    h=mid-1
                else:
                    h=mid
                    l=mid+1
            if h<0:
                h=0
            a.append(abs(p[h]-(i*(h+1)))+abs((p[-1]-p[h]-(i*(len(p)-h-1)))))
        return a
        
