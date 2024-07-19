class Solution:
    def luckyNumbers (self, m: List[List[int]]) -> List[int]:
        a=[0]*len(m)
        for i in range (len(a)):
            a[i]=min(m[i])
        b=[0]*len(m[0])
        for i in range (len(m[0])):
            for j in range (len(m)):
                b[i]=max(b[i],m[j][i])
        ans=[]
        for i in range (len(m)):
            for j in range (len(m[i])):
                if m[i][j]==a[i] and m[i][j]==b[j]:
                    ans.append(m[i][j])         
        return ans