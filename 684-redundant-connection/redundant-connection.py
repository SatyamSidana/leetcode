class Solution:
    def findRedundantConnection(self, e: List[List[int]]) -> List[int]:
        p=[0]*(len(e)+1)
        for i in range (1,len(p)):
            p[i]=i
        
        rank = [1]*(len(e)+1)
        def find(x):
            # print(x,p[x])
            if p[x]==x:
                return x
            else:
                return find(p[x])
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2:
                return True
            if rank[p1]>=rank[p2]:
                p[p2]=p1
                rank[p1]+=rank[p2]
            else:
                p[p1]=p2
                rank[p2]+=rank[p1]
            return False
        for i in e:
            if union(i[0],i[1]):
               return i 
            
        
        
        