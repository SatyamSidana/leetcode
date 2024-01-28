class Solution:
    def isMonotonic(self, n: List[int]) -> bool:
        if len(n)==1:
            return True
        else:
            j=0
            if n[0]==n[1]:
                while  j<len(n)-1:
                    if n[j]==n[j+1]: 
                        j+=1
                    else:
                        break
            if j==len(n)-1:
                return True
            print(j)
            if n[j]>n[j+1]:
                for i in range (j,len(n)-1):
                    if n[i+1]>n[i]:
                        return False
            if n[j]<n[j+1]:
                for i in range (j,len(n)-1):
                    if n[i+1]<n[i]:
                        return False
        return True

        