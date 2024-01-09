class Solution:
    def nextGreaterElement(self, n1: List[int], n2: List[int]) -> List[int]:
        b=[]
        a={}
        for i in range (len(n2)):
            a[n2[i]]=i
        for i in range (len(n1)):
            t=True
            for j in range (a[n1[i]]+1,len(n2)):
                if n2[j]>n1[i]:
                    b.append(n2[j])
                    t=False
                    break
            if t:
                b.append(-1)
        return b
            

        
        