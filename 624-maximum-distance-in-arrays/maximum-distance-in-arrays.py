class Solution:
    def maxDistance(self, arr: List[List[int]]) -> int:
        a=[]
        b=[]
        for i in range(len(arr)):
            a.append([arr[i][0],i])
            b.append([arr[i][-1],i])
        a.sort()
        b.sort()
        if a[0][1]==b[-1][1]:
            return max(abs(a[0][0]-b[-2][0]),abs(a[1][0]-b[-1][0]))
        return abs(a[0][0]-b[-1][0])
            
