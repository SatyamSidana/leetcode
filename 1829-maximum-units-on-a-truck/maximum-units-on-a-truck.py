class Solution:
    def maximumUnits(self, b: List[List[int]], t: int) -> int:
        def swap(s):
            temp=s[0]
            s[0]=s[1]
            s[1]=temp
        c=0
        for i in b:
            swap(i)
        b.sort(reverse=True)
        for i in b:
            if i[1]<t:
                c+=i[0]*i[1]
                t-=i[1]
            else:
                c+=i[0]*t
                break
        return c