class Solution:
    def numTeams(self, rating: List[int]) -> int:
        dp1=[]
        for i in range (len(rating)):
            dp1.append([])
            for j in range(3):
                dp1[i].append([0]*2)

        def dp(i, depth, reverse=True):
            if depth == 0: return 1
            if dp1[i][depth][reverse]!=0:
                return dp1[i][depth][reverse]
            res = 0
            for j in range(i + 1, len(rating)):
                if (reverse and rating[j] > rating[i]) or (not reverse and rating[j] < rating[i]):
                    res += dp(j, depth - 1, reverse)
            dp1[i][depth][reverse]=res
            return res

        res = 0
        for i in range(len(rating)):
            res += dp(i,2, reverse=True) 
            res += dp(i,2, reverse=False)
        return res
