class Solution:
    def findCircleNum(self, c: List[List[int]]) -> int:
        p=0
        v=[0]*len(c)
        e=collections.deque()
        for i in range (len(c)):
            if v[i]==1:
                pass
            else:
                e.append(i)
                v[i]=1
                while e:
                    b=e.popleft()
                    for j in range (len(c[0])):
                        if c[b][j]==1 and v[j]==0:
                            v[j]=1
                            e.append(j)
                p+=1
        return p

                
        
        