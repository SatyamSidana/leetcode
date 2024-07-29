class Solution:
    def minimumCost(self, o: str, ch: str, s: List[str], t: List[str], c: List[int]) -> int:
        a=[[float('inf')] * 26 for _ in range(26)]
        x=ord("a")
        for i in range (26):
            a[i][i]=0
        for i in range (len(s)):
            a[ord(s[i])-x][ord(t[i])-x]=min(a[ord(s[i])-x][ord(t[i])-x],c[i])
        for k in range (26):
            for i in range(26):
                for j in range(26):
                    a[i][j]=min(a[i][j],a[i][k]+a[k][j])
        res = sum(a[ord(s) - ord('a')][ord(t) - ord('a')] for s, t in zip(o, ch))
        return res if res != float('inf') else -1