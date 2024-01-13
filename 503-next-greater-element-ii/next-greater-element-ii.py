class Solution:
    def nextGreaterElements(self, n: List[int]) -> List[int]:
        a=[]
        for i in range (len(n)):
            t=True 
            for j in range (i+1,len(n)):
                if n[j]>n[i] :
                    a.append(n[j])
                    t=False
                    break
            if t:
                for j in range (0,i):
                    if n[j]>n[i] :
                        a.append(n[j])
                        t=False
                        break
            if t :
                a.append(-1)
        return a
        
        