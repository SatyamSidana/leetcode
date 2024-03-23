class Solution:
    def removeDuplicates(self, n: List[int]) -> int:
        a=0
        b=2
        while(b<len(n)):
            if n[a]==n[b]:
                while  b<len(n) and n[a]==n[b] :
                    n.pop(b)
            a+=1
            b+=1
        return b


            
                

        