class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        a={}
        b=[]
        mi=0
        ma=0
        for i in range (len(s)):
            a[s[i]]=i
        print(a)
        for i in range (len(s)):
            ma=max(ma,a[s[i]])
            if i==ma:
                b.append(ma-mi)
                mi=i
        b[0]+=1    
        return b
        