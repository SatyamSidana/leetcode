class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        a={}
        ans=[]
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        b=sorted(a.items(),key=lambda x: (x[1],-x[0]))
        for i in b:
            for j in range (i[1]):
                ans.append(i[0])
        return ans