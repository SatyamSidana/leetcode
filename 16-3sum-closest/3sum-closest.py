class Solution:
    def threeSumClosest(self, n: List[int], t: int) -> int:
        n.sort()
        m=1e9
        ans=0
        for i in range (len(n)-2):
            if i>0 and n[i]==n[i-1]:
                continue
            l=i+1
            h=len(n)-1
            while l<h:
                temp=n[l]+n[h]+n[i]
                if temp>t:
                    h-=1
                    if abs(temp-t)<m:
                        m=abs(temp-t)
                        ans=temp
                elif temp<t:
                    l+=1
                    if abs(temp-t)<m:
                        m=abs(temp-t)
                        ans=temp
                else:
                    return t
        return ans