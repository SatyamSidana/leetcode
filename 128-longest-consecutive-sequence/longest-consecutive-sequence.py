class Solution:
    def longestConsecutive(self, n: List[int]) -> int:
        a={}
        for i in n:
            a[i]=1
        m=0
        for i in n:
            if a[i]==1:
                c=0
                b=True
                j=1
                while b:
                    if a.get(i+j):
                        c+=1
                        a[i+j]=0
                        j+=1
                    else:
                        b=False
                b=True
                j=1
                while b:
                    if a.get(i-j):
                        c+=1
                        a[i-j]=0
                        j+=1
                    else:
                        b=False
                a[i]=0
                m=max(m,c+1)
        return m
                
                    
                



        