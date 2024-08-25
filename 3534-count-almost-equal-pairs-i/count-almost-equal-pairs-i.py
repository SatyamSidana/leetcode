class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def check(a,b):
            while len(a)<len(b):
                a="0"+a
            while len(b)<len(a):
                b="0"+b
            f=-1
            s=-1
            c=0
            for i in range (len(a)):
                if a[i]!=b[i]:
                    c+=1
                    if c==1:
                        f=i
                    elif c==2:
                        s=i
                    else:
                        break
            a=list(a)
            a[f],a[s]=a[s],a[f]
            a="".join(a)
            return a==b
        n=[]
        for i in nums:
            n.append(str(i))
        c=0
        for i in range (len(n)):
            for j in range (i+1,len(n)):
                if check(n[i],n[j]):
                    c+=1
        return c
