class Solution:
    def countNicePairs(self, n: List[int]) -> int:
        def rev(a):
            b=0
            while a!=0:
                digit = a % 10
                b = b* 10 + digit
                a //= 10
            return b
        d={}
        c=0
        for i in n:
            if d.get((i-rev(i))):
                c+=d[(i-rev(i))]
                d[(i-rev(i))]+=1
            else:
                d[(i-rev(i))]=1
        return c%((10**9) + 7)
