class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        if d=="":
            return []
        n=len(d)
        a={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans=[]
        def f(i,s):
            if i==n:
                ans.append(s)
                return 0
            for j in a[d[i]]:
                x=f(i+1,s+j)
            return 1
        f(0,"")
        return ans



        