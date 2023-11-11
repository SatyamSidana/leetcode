class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        a=""
        b=min(s)
        for i in range (len(b)):
            for j in s:
                if b[i]==j[i]:
                    pass
                else:
                    return a
            a+=b[i]
        return a
            


        

        