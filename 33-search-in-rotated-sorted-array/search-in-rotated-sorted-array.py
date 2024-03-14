class Solution:
    def search(self, n: List[int], t: int) -> int:
        if len(n)==1:
            if n[0]==t:
                return 0
            else:
                return -1
        s=False
        for i in range (len(n)-1):
            if n[i]>n[i+1]:
                b=i+1
                s=True
                break
        if s:
            l1=0
            h1=b-1
            l2=b
            h2=len(n)-1
            while(l1<=h1):
                mid=(h1+l1)//2
                if n[mid]<t:
                    l1=mid+1
                elif n[mid]>t:
                    h1=mid-1
                else:
                    return mid
            while(l2<=h2):
                mid=(h2+l2)//2
                if n[mid]<t:
                    l2=mid+1
                elif n[mid]>t:
                    h2=mid-1
                else:
                    return mid
        else:
            l1=0
            h1=len(n)-1
            while(l1<=h1):
                mid=(h1+l1)//2
                if n[mid]<t:
                    l1=mid+1
                elif n[mid]>t:
                    h1=mid-1
                else:
                    return mid
        return -1