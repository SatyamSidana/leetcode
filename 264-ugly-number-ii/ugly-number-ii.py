class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans=[]
        for i in range(33) : 
            for j in range(22):
                for k in range(17):
                    ans.append((2**i) * (3**j) * (5**k))
        ans.sort()
        return ans[n-1]
        