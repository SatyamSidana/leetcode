class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i=0
        j=1
        k=2
        while k<len(arr):
            if  arr[i]%2==1 and arr[j]%2==1 and arr[k]%2==1:
                return True
            i+=1
            j+=1
            k+=1
        return False
        