class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a=defaultdict(int)
        for i in edges:
            a[i[0]]+=1
            a[i[1]]+=1
        for i in a:
            if a[i]==len(edges):
                return i