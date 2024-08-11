class Solution:
    def countGoodNodes(self, e: List[List[int]]) -> int:
        a=[]
        n=len(e)+1
        for i in range (n):
            a.append([])
        for i in e:
            a[i[0]].append(i[1])
            a[i[1]].append(i[0])
        self.ans=0
        def dfs(s,p):
            if len(a[s])==0:
                self.ans+=1
                return 1
            else:
                x=-1
                c=0
                t=True
                for i in range (len(a[s])):
                    if a[s][i]!=p:
                        if x==-1:
                            x=dfs(a[s][i],s)
                            c+=x
                        else:
                            y=dfs(a[s][i],s)
                            if x!=y:
                                t=False
                            c+=y
                if t:
                    self.ans+=1
                return c+1
        dfs(0,-1)
        return self.ans


