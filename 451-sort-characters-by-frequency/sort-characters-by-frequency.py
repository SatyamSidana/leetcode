class Solution:
    def frequencySort(self, s: str) -> str:
        a={}
        b=""
        for i in s:
            if i in a:
                a[i]+=1
            else:
                a[i]=1

        d=sorted(a.items(), key = lambda x : x[1] , reverse=True)
        
        for (i,j) in d:
            for k in range (j):
                b+=i

  
        return b