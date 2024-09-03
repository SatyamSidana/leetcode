class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def f(i,r,s):
            if i==n and r==0:
                ans.append(s)
                return 0
            if i<n:
                if r>0:
                    return f(i,r-1,s+")")+f(i+1,r+1,s+"(")
                else:
                    return f(i+1,r+1,s+"(")
            else:
                return f(i,r-1,s+")")
        f(0,0,"")
        return ans