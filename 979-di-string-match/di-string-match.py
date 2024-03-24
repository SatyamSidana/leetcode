class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        def swap(x,y):
            temp=a[x]
            a[x]=a[y]
            a[y]=temp
        a=[]
        for i in range (len(s)+1):
            a.append(i)
        i=0
        c=0
        t=False
        while i<len(s):
            if s[i]=="I":
                i+=1
            elif s[i]=="D":
                swap(i,i+1)
                j=i-1
                while j>=0 and s[j]=="D":
                    swap(j,j+1)
                    j-=1
                i+=1
        return a
                

        