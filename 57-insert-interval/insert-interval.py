class Solution:
    def insert(self, n: List[List[int]], p: List[int]) -> List[List[int]]:
        a=[]
        if len(n)==0:
            a.append(p)
            return a
        if p[0]>n[len(n)-1][1]:
            n.append(p)
            return n
        if p[1]<n[0][0]:
            a.append(p)
            return a+n
        for i in range (len(n)):
            if n[i][1]<p[0]:
                pass
            else:
                j=i
                while j<len(n) and n[j][0]<=p[1]:
                    j+=1
                print(j)
                d=[min(n[i][0],p[0]),max(n[j-1][1],p[1])]
                c=i
                break
        x=0
        while x<c:
            a.append(n[x])
            x+=1
        a.append(d)
        while j<len(n):
            a.append(n[j])
            j+=1
        return a

        