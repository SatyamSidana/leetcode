class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a={}
        for i in allowed:
            a[i]=1
        ans=0
        for i in words:
            t=True
            for j in i:
                if j not in a:
                    t=False
            if t:
                ans+=1
        return ans