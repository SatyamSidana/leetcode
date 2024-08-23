class Solution:
    def findComplement(self, n: int) -> int:
        ans=""
        while n>0:
            if (n&1)==1:
                ans="0"+ans
            else:
                ans="1"+ans
            n=n>>1
        print(ans)
        return int(ans,2)