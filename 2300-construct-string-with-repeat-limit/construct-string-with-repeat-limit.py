class Solution:
    def repeatLimitedString(self, s: str, r: int) -> str:
        a=[0]*26
        n=ord("a")
        for i in s:
            a[ord(i)-n]+=1
        i=25
        j=24
        ans=""
        while i>=0:
            while a[i]>0:
                x=min(r,a[i])
                ans+=(chr(i+n))*x
                a[i]-=x
                if a[i]>0:
                    t=True
                    while t:
                        if j<0:
                            return ans
                        if a[j]>0:
                            ans+=chr(j+n)
                            a[j]-=1
                            t=False
                        else:
                            j-=1
            i=j
            j-=1
        return ans
            
                    


