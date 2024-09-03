from sortedcontainers import SortedList, SortedSet, SortedDict 
class Solution:
    def resultsArray(self, q: List[List[int]], k: int) -> List[int]:
        a=SortedList()
        ans=[]
        for i in q:
            x=abs(i[0])+abs(i[1])
            a.add(x)
            if len(a)<k:
                ans.append(-1)
            else:
                ans.append(a[k-1])
        return ans