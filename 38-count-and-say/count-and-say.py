class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(s):
            c=1
            i=0
            ans=""
            while i<len(s)-1:
                if s[i]==s[i+1]:
                    c+=1
                    i+=1
                else:
                    ans+=str(c)+s[i]
                    c=1
                    i+=1
            return ans+str(c)+s[-1]
        x="1"
        for i in range(n-1):
            x=rle(x) 
        return x           

        