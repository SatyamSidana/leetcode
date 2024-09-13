class Solution:
    def minOperations(self, k: int) -> int:
        if k<2:
            return 0
        a=1
        ans=0
        while True:
            if ceil(k/a)==ceil(k/(a+1)):
                ans+=ceil(k/a)-1
                break
            else:
                a+=1
                ans+=1
        return ans