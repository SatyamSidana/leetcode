class Solution:
    def compressedString(self, w: str) -> str:
        i=0
        ans=""
        while i<len(w):
            c=0
            s=w[i]
            while i<len(w) and c<9 and w[i]==s:
                i+=1
                c+=1
            ans+=str(c)+s
        return ans