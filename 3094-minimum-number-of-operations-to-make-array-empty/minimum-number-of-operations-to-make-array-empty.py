class Solution:
    def minOperations(self, n: List[int]) -> int:
        a={}
        for i in n:
            if a.get(i):
                a[i]+=1
            else:
                a[i]=1
        m=0
        for i in a:
            b=a[i]
            if b==1:
                return -1
            else:
                if b%3==0:
                    m+=b//3
                else:
                    m+=(b//3)+1
        return m

        