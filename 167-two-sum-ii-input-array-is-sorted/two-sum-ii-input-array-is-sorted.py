class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        def b(l,h,s):
            while l<=h:
                mid=(l+h)//2
                if n[mid]>s:
                    h=mid-1
                elif n[mid]<s:
                    l=mid+1
                else:
                    return mid
            return -1
        for i in range(len(n)):
            if b(i+1,len(n)-1,t-n[i])!=-1:
                return [i+1,b(i+1,len(n)-1,t-n[i])+1]
        
        
