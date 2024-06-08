class Solution:
    def commonChars(self, w: List[str]) -> List[str]:
        a={}
        b={}
        ans=[]
        for i in range (len(w[0])):
            if w[0][i] in a:
                a[w[0][i]]+=1
            else:
                a[w[0][i]]=1
        for i in range (1,len(w)):
            for j in range (len(w[i])):
                if w[i][j] in a and a[w[i][j]]>0:
                    if w[i][j] in b:
                        b[w[i][j]]+=1 
                    else:
                        b[w[i][j]]=1
                    a[w[i][j]]-=1
            a=b
            b={}
        for i in a:
            for j in range (a[i]):
                ans.append(i)
        return ans